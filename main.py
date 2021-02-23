
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
if __name__ == '__main__':
    data = DataManipulation()
    data.inputData()
    #data.data_analyzis([1,2,3,5,9,2,4,6])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
