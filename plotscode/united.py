import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri

def main():
    categories = ["takeoff", "right", "left", "land", "forward", "backward"]
    base_r_script_path = "/Avatar/plots"

    for category in categories:
        # Construct the path to the R script
        r_script_path = f"{base_r_script_path}/{category}.R"

        try:
            # Load and execute the R script
            print(f"Executing R script: {r_script_path}")
            robjects.r.source(r_script_path)
            print(f"R script for {category} executed successfully.")
        except Exception as e:
            print(f"An error occurred while executing the R script for {category}: {e}")
            continue

        # Access the BrainWaveAnalysis class from R
        BrainWaveAnalysis = robjects.globalenv['BrainWaveAnalysis']
        
        # Construct the path to the category's data files
        file_path = f"/Avatar/plots/plot_waves/brainwaves-csv/{category}"
        print(f"Processing data in: {file_path}")

        # Create an instance of the BrainWaveAnalysis class
        try:
            analysis = BrainWaveAnalysis(file_path)
        except Exception as e:
            print(f"An error occurred while initializing BrainWaveAnalysis for {category}: {e}")
            continue

        # Invoke methods or attributes of the R6 class, e.g., plot_data
        try:
            analysis.plot_data()
            print(f"Plotting completed for {category}")
        except Exception as e:
            print(f"An error occurred while plotting data for {category}: {e}")

if __name__ == "__main__":
    main()
