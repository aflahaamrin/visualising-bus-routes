from filter_bus_data import main as filter
from plot_bus_map import main as plot

def main():
    """
    to see result for different route, 
    open trips.txt file inside data\raw\metlink_bus folder and copy paste another trip id
    """
    filter("2__1__252__NBM__19__2__19__2_20251005")
    plot()

if __name__ == "__main__":
    main()