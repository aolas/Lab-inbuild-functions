
#1 Write a program that asks the user to enter comma-separated digits. Write data management exceptions.
# Using Python built-in functions output to the screen: sum of digits entered, maximum and minimum values,
# values which index is between 2 and 4, number of numbers entered, values greater than 10, list in ascending
# and descending order, and "inverted "list entered.
class DataManipulation:
    def inputData(self):
    # Use a breakpoint in the code line below to debug your script.
        input_string = input("Enter string of numbers seperated by , : ")
        valid_data = self.data_sanatization(input_string)
        if len(valid_data)> 0:
            self.data_analyzis(valid_data)
        else:
            print("No data to analyze")

    def data_sanatization(self,input_list):
        input_list = input_list.split(",")
        new_list = []
        for i in range(0, len(input_list)):
            try:
                new_list.append(int(input_list[i]))
            except ValueError as e:
                print("Can't convert this input:", input_list[i])
        print("Sanityzed data", new_list)
        return new_list
    def data_analyzis(self, input_list):
        index_min = min(range(len(input_list)), key=input_list.__getitem__)
        index_max = max(range(len(input_list)), key=input_list.__getitem__)
        input_item_count =len(input_list)
        greater_than_10 = []
        print("Sum of digits entered:", sum(input_list))
        print("MIN pozition:", index_min, "value:", input_list[index_min])
        print("MAX pozition:", index_max, "value:", input_list[index_max])
        if input_item_count > 4:
            print("Values which index is between 2 and 4,", input_list[2:4])
        else:
            print("Cant slice between 2 and 4, no enough  items")
        print("Input",input_list)
        input_list.reverse()
        print("inverted list:", input_list)
        input_list.sort(reverse=False)
        print("Sorted ascending order:", input_list)
        input_list.sort(reverse=True)
        print("Sorted descending order:", input_list)
        for ind in range(0, len(input_list)):
            if input_list[ind] > 10:
                greater_than_10.append(input_list[ind])
        print("Items greater than 10", greater_than_10)
# Press the green button in the gutter to run the script.
class Data_Manipulation_Part2:
    """Sort the  list   by    item     length in ascending and descending    order."""
    def list_sort(self):
        sort_me = ["Kaunas", "Vilnius", "Alytus", "Klaipeda","as" ,"Varena", "Druskininkai", "Klaipeda"]
        sorted_list = sorted(sort_me, key=len)
        #sort_me.sort(key=len)
        print("before sort:", sort_me)
        print("after sort", sorted_list)

class Data_Manipulation_Part3:
    """Perform list element transformation: 1. by using formula: x = x * (x - 10), 2. square each element."""
    def data_manipulation(self):
        my_list = [12, 45, 23, 56, -546, 34]
        print(my_list)
        for ind in range(0, len(my_list)):
            my_list[ind] = my_list[ind]* (my_list[ind] -10)
        print("After modification by formula x=x*(x-10):", my_list)
        for ind in range(0, len(my_list)):
            my_list[ind] = my_list[ind]**2
        print("After square:", my_list)
class Data_Manipulation_Part4:
    """4. Sort the dictionary according to the second item in the value list in ascending and descending order. """
    def data_manipulation(self):
        sort_me = {
            "a": [7, 1, 9],
            "b": [8, -4, 3],
            "c": [9, 10, 151],
            "d": [-3, 9, 11]
        }
        sort_2 = {
            "a": 1,
            "b": -5,
            "c": 55,
            "d": 11
        }
        print("Before ", sort_me)
        #dict(sorted(sort_me.items(), key=lambda item: item[1]))
        aa = sorted(sort_me.items(), key=lambda x: x[1][1])    # soting by item second value
        print("Sort me dictionary", aa)


if __name__ == '__main__':
    #part1 = DataManipulation()
    #part1.inputData()
    #part2 = Data_Manipulation_Part2()
    #part2.list_sort()
    #part3 = Data_Manipulation_Part3()
    #part3.data_manipulation()
    part4 = Data_Manipulation_Part4()
    part4.data_manipulation()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
