-- Drop any previous versions of the table that may exist
DROP TABLE IF EXISTS participants;

-- Create table called 'participants'
CREATE TABLE participants (
	id SERIAL PRIMARY KEY,
	gender VARCHAR NOT NULL,
	age FLOAT NOT NULL,
	height_m FLOAT NOT NULL,
	weight_kg FLOAT NOT NULL,
	family_history_with_overweight BOOLEAN NOT NULL,
	high_calorie_intake BOOLEAN NOT NULL,
	vegetable_consumption FLOAT NOT NULL,
	daily_meal_count FLOAT NOT NULL,
	food_between_meals VARCHAR NOT NULL,
	smoking_habit BOOLEAN NOT NULL,
	water_consumption FLOAT NOT NULL,
	tracks_daily_calories BOOLEAN NOT NULL,
	exercise_frequency FLOAT NOT NULL,
	tech_usage_time FLOAT NOT NULL,
	alcohol_intake VARCHAR NOT NULL,
	transportation_used VARCHAR NOT NULL,
	obesity_level VARCHAR NOT NULL
);

--After importing data into the tables from their respective .csv files via the pgAdmin Import/Export tool, verify that the data populated correctly
SELECT * FROM participants