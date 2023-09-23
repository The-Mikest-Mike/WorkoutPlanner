# constants
DAYS_OF_WEEK = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

# classes 
class Exercise:
    def __init__(self, name, sets, reps, weight=None):
        self.name = name
        self.sets = sets
        self.reps = reps
        self.weight = weight

# exercise categories
EXERCISE_CATEGORIES = {
    "legs": ["Squats/step front lunges/walking lunges alternate", "Calf Rises"],
    "core": ["Hanging Leg Rises", "half wipers", "plank 4x10secs"],
    "chest": ["Incline dumbell press", "Close grip flat bench", "5 slow push ups", "straight push-ups 10 x 4"],
    "back": ["Bent Over Row", "Deadlift"],
    "shoulder": ["Dumbbell shoulder press seated", "Lateral Raises", "Medicine Ball Front Raises 4x15"],
    "tricep": ["Overhead tricep extension", "one hand on bench overhead tricep extension", "Mule Kick"],
    "bicep": ["Dumbbell curl standing or seated on decline bench supinated", "Pull-ups neutral grip 4x6"],
    "forearm": ["Forearm", "Forearm Reverse wrist curls", "Front wrist lifts 4x20"],
    "extra": ["Walk to the river", "Train to Failure: Forearm twists 15lb", "Joggling to the river", "30 min static bike lvl 1", "2km run - 23min", "Yoga"]
}

class WorkoutDay:
    def __init__(self, day_of_week, exercises):
        self.day_of_week = day_of_week
        self.exercises = exercises

# functions
def print_workout(workout_day):
    print(f"{workout_day.day_of_week.capitalize()}:")
    for category, exercise_list in EXERCISE_CATEGORIES.items():
        print(f"    {category.upper()}:")
        for exercise in workout_day.exercises:
            if exercise.name in exercise_list:
                if exercise.weight:
                    print(f"        {exercise.name} {exercise.sets}x{exercise.reps} at {exercise.weight}lb")
                else:
                    print(f"        {exercise.name} {exercise.sets}x{exercise.reps}")


# creating instances of WorkoutDay for each day of the week and add exercises accordingly

# monday
monday_exercises = [
    Exercise("Squats/step front lunges/walking lunges alternate", 4, 10, "30lbs"),
    Exercise("Calf Rises", 1, 86, "kg"),
    Exercise("Hanging Leg Rises", 4, 10)
]
monday = WorkoutDay("monday", monday_exercises)

# tuesday
tuesday_exercises = [
    Exercise("Incline dumbbell press", 4, 10, "40lb"),
    Exercise("Close grip flat bench", 4, 10, "35lb"),
    Exercise("5 slow push ups", 1, 5),
    Exercise("half wipers", 1, 1),
]
tuesday = WorkoutDay("tuesday", tuesday_exercises)

# wednesday
wednesday_exercises = [
    Exercise("Bent Over Row", 4, 10, "35lb"),
    Exercise("Deadlift", 4, 10, "35lb"),
    Exercise("plank", 4, 10),
    Exercise("Calf Rises", 1, 86, "kg"),
]
wednesday = WorkoutDay("wednesday", wednesday_exercises)

# thursday
thursday_exercises = [
    Exercise("Dumbbell shoulder press seated", 4, 10, "25lb"),
    Exercise("Lateral Raises", 4, 10, "20lb"),
    Exercise("Medicine Ball Front Raises", 4, 15, "10lb"),
]
thursday = WorkoutDay("thursday", thursday_exercises)

# friday
friday_exercises = [
    Exercise("Overhead tricep extension", 4, 10, "45lb"),
    Exercise("one hand on bench overhead tricep extension", 4, 10, "15lb"),
    Exercise("Mule Kick", 1, 10),
    Exercise("Dumbbell curl standing or seated on decline bench supinated", 4, 10, "20lb"),
    Exercise("Pull-ups neutral grip", 4, 6),
    Exercise("30 min static bike", 1, 1, "lvl 1"),
]
friday = WorkoutDay("friday", friday_exercises)

# saturday
saturday_exercises = [
    Exercise("Train to Failure: Forearm", 1, 1, "15lb"),
    Exercise("Forearm Reverse wrist curls", 1, 1, "5lb"),
    Exercise("Front wrist lifts", 4, 20, "5lb"),
    Exercise("straight push-ups", 10, 4),
]
saturday = WorkoutDay("saturday", saturday_exercises)

# sunday
sunday_exercises = [
    Exercise("Deadlift", 4, 10, "40lb"),
    Exercise("2km run", 1, 1, "23min"),
]
sunday = WorkoutDay("sunday", sunday_exercises)

# main program
if __name__ == "__main__":
    # Creating a list of all the WorkoutDay instances
    workout_days = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]
    
    # You can print the workout for each day of the week using the print_workout function.
    for day in DAYS_OF_WEEK:
        for workout_day in workout_days:
            if workout_day.day_of_week.lower() == day:
                print_workout(workout_day)
