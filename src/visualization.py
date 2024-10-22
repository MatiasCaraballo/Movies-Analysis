import matplotlib.pyplot as plt
from utils.save_file import save_file

from utils.error_handler import error_handler
import seaborn as sns
load = save_file()
error = error_handler()
class visualization:

    def plot_data(self,data,first_value,second_value,title,xlabel,ylabel):

        plt.figure(figsize=(10, 5))
        plt.plot(data[first_value], data[second_value], marker='o')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        load.save_plot(title)

    def top_list(self,bar_type,first_value,second_value,title):
        match bar_type:
            case "bar":
                plt.bar(first_value, second_value, color='blue')
            case "barh":
                plt.barh(first_value, second_value, color='blue')
            case _:
                error.value_error()

        plt.title(title)
        plt.xlabel(first_value)
        plt.ylabel(second_value)
        plt.tight_layout()
        plt.show()
        load.save_plot(title)

    def gauss_function(self,df,title,xlabel,ylabel):
        sns.histplot(df, kde=True)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()
        load.save_plot(title)

