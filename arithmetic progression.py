my_terms = {}
my_list = []
num = 0
stat = "run"
cd_dicto = {}

def take_inputs():

    global num


    while True:
        term = input("Enter your term: (Enter q to quit)")

        if term == "q":
            break

        if term != "q":
            num = int(num)
            num += 1
            num = str(num)

            term_name = "term" + num
            my_terms.update({term_name: term})


def common_difference():
     global i
     global z
     global length
     global stat
     global num
     global cd
     global list_ap

     list_ap = []

     num = 0

     i = len(my_list)
     z = i - 1
     length = i +1

     for items in my_terms.values():
         my_list.append(items)

     while stat == "run":

         for a in range(length):
             num += 1
             c = "cd" + str(num)

             cd = int(my_list[i]) - int(my_list[z])

             cd_dicto.update({c : cd})

             i -=1

             if i < 0:
                 stat = "terminate"

             for another_item in cd_dicto.values():
                list_ap.append(another_item)

             print(cd_dicto)
             print(list_ap)

def check_for_ap():
    global check_v
    check_v = len(cd_dicto)
    global ap

    for cap in range(len(cd_dicto)):
        h = int(list_ap[0])
        capd = cap + 1
        h1 = int(list_ap[1])
        if h == h1:
            ap = "positive"
        if h != h1:
            ap = "negative"

        if ap =="negative":
            print("The given terms ar not an Arithmetic Progression")

        if ap == "positive":
            print(cd)




def find_nth_term():
    global n
    n = int(input("Which term do you want to find? : "))

    formulae_n = n - 1

    if n > length:
        nth_term = my_list[0] +  formulae_n * cd
        print("The "+str(n)+"th term is: ",nth_term)

take_inputs()
common_difference()
#check_for_ap()
find_nth_term()