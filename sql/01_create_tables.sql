CREATE TABLE pokemons (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    height INTEGER,
    weight INTEGER,
    base_expirience INTEGER,
    types TEXT[],
    loaded_at TIMESTAMP DEFAULT NOW()
);