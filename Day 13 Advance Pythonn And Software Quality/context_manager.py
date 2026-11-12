class TaskProcessingManager:

    def __enter__(self):
        print("\n========== TASK PROCESSING STARTED ==========")
        return self

    def __exit__(self, exc_type, exc_value, traceback):

        print("\n========== TASK PROCESSING FINISHED ==========")

        if exc_type:
            print("Error occurred:", exc_value)

        return False