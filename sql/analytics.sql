-- 1. Топ 10 покемонов по base_experience

SELECT 
	id,
	name,
	base_experience
FROM 
	pokemons
WHERE
	base_experience IS NOT NULL
ORDER BY 
	base_experience DESC
LIMIT 10

-- 2. Средний рост и вес покемонов в группировке по base_exp

SELECT
	unnest(types) AS type,
	count(*) AS pokemon_count,
	round(AVG(weight)::numeric, 2) as avg_weight,
	round(AVG(height)::numeric, 2) as avg_height
FROM
	pokemons
GROUP BY
	type
ORDER BY 
	pokemon_count desc
	
-- 3. Топ 3 покемонов по каждому типу (оконные функции)    -- 
WITH ranked AS (
	SELECT
		id,
		name,
		base_experience,
		unnest(types) AS type,
		ROW_NUMBER() OVER (
			PARTITION BY unnest(types)
			ORDER BY base_experience DESC
		) AS rn
	FROM pokemons
	WHERE base_experience IS NOT NULL
)
SELECT
	type,
	rn,
	id,
	name,
	base_experience
FROM 
	ranked
WHERE
	rn <= 3
ORDER BY 
	type, rn
	
-- 4. Покемоны с несколькими типами (агрегация массивов, сортировка по кол-ву)
SELECT
	id,
	name,
	types,
	array_length(types, 1) AS types_count
FROM
	pokemons
WHERE
	array_length(types, 1) > 1
ORDER BY 
	types_count DESC, 
	id
LIMIT 10

-- 5. Распределение покемонов по весовым категориям (CASE, агрегация)
SELECT
	CASE
		WHEN weight < 100 THEN 'легкие (<100)'
		WHEN weight < 500 THEN 'средние (100 - 500)' 
		WHEN weight < 1000 THEN 'тяжелые (500 - 1000)'
		ELSE 'очень тяжелые (1000+)'
	END AS weight_category,
	COUNT(*) AS pokemon_count,
	ROUND(AVG(base_experience)::numeric, 2) AS avg_base_exp
FROM
	pokemons
GROUP BY weight_category
ORDER BY pokemon_count DESC
	

	

	


