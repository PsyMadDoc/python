# 1. First, take a minute to inspect the string daily_sales in the code editor.
# How is each transaction stored? How is each piece of data within the transaction stored?
# Start thinking about how we can split up this string into its individual pieces of data.

# 2.It looks like each transaction is separated from the next transaction by a ,, and then each piece of data within a transaction is separated by the artifact ;,;.
# If we want to split up daily_sales into a list of individual transactions, we are going to want to split by ,, but first, we need to replace the artifact ;,; to something without a comma, so we don’t split any transactions themselves.
# Replace all the instances of ;,; in daily_sales with some other character and save the result to daily_sales_replaced.

# 3.Now we can split the string into a list of each individual transaction.
# Split daily_sales_replaced around commas and save it to a new list daily_transactions.

# 4.Print daily_transactions.
# How does it look?

# 5.Our next step is to split each individual transaction into a list of its data points.
# First, define an empty list daily_transactions_split

# 6.Now, iterate through daily_transactions (remember, this is a list of strings currently), and for each transaction, split the string around whatever character you replaced the ;,; artifacts with in Step 2.
# Append each of these split strings (which are lists now) to our new list daily_transactions_split.

# 7.Print daily_transactions_split.
# How’s it looking?

# 8.It looks like each data item has inconsistent whitespace around it. First, define an empty list transactions_clean.
# Now, Iterate through daily_transactions_split and for each transaction iterate through the different data points and strip off any whitespace.
# Add each of these cleaned up transactions to the new list transactions_clean.

# 9.Print transactions_clean.
# If you performed the last step correctly, you shouldn’t see any unnecessary whitespace.

# 10.Create three empty lists. customers, sales, and thread_sold. We are going to collect the individual data points for each transaction in these lists.

# 11.Now, iterate through transactions_clean and for each transaction:
# Append the customers name to customers.
# Append the amount of the sale to sales.
# Append the threads sold to thread_sold.

# 12.Print customers, sales, and thread_sold to make sure each list is what you are expected.
# Determine the total value of the days sales.

# 13.Now we want to know how much Thread Shed made in a day.
# First, define a variable called total_sales and set it equal to 0.

# 14.Now, consider the list sales. It is a list of strings that we want to sum. In order for us to sum these values, we will have to remove the $, and set them equal to floats.
# Iterate through sales and for each item, strip off the $, set it equal to a float, and add it to total_sales

# 15.Print total sales.
# How much did we make today?
# How much thread of any specific color was sold?

# 16.Finally, we want to determine how many of each color thread we sold today. Let’s start with a single color, and then we’ll generalize it.
# First, print out thread_sold and inspect it.

# 17.We see that thread_sold is a list of strings, some are single colors and some are multiple colors separated by the & character.
# The end product we want here is a list that contains an item for each color thread sold, so no strings that have multiple colors in them.
# First, define an empty list thread_sold_split.

# 18.Next, iterate through thread_sold. For each item, check if it is a single color or multiple colors. If it is a single color, append that color to thread_sold_split.
# If it is multiple colors, first split the string around the & character and then add each color indivudally to thread_sold_split.

# 19.Great, now we have a list thread_sold_split that contains an entry with the color of every thread sold today.
# Define a function called color_count that takes one argument, color. The function should iterate through thread_sold_split and count the number of times the item is equal to argument, color. Then, it should return this count.

# 20.Test your new function by running color_count('white').
# Your function should return 28.

# 21.Define a list called colors that stores all of the colored threads that Thread Shed offers:
# py colors = ['red','yellow','green','white','black','blue','purple']

# 22.Now, using the list colors, the string method .format(), and the function color_count, iterate through thread_sold_split and print a sentence that says how many threads of each color were sold today.


daily_sales = \
    """Edith Mcbride   ;,;$1.21   ;,;   white ;,; 
09/15/17   ,Herbert Tran   ;,;   $7.29;,; 
white&blue;,;   09/15/17 ,Paul Clarke ;,;$12.52 
;,;   white&blue ;,; 09/15/17 ,Lucille Caldwell   
;,;   $5.13   ;,; white   ;,; 09/15/17,
Eduardo George   ;,;$20.39;,; white&yellow 
;,;09/15/17   ,   Danny Mclaughlin;,;$30.82;,;   
purple ;,;09/15/17 ,Stacy Vargas;,; $1.85   ;,; 
purple&yellow ;,;09/15/17,   Shaun Brock;,; 
$17.98;,;purple&yellow ;,; 09/15/17 , 
Erick Harper ;,;$17.41;,; blue ;,; 09/15/17, 
Michelle Howell ;,;$28.59;,; blue;,;   09/15/17   , 
Carroll Boyd;,; $14.51;,;   purple&blue   ;,;   
09/15/17   , Teresa Carter   ;,; $19.64 ;,; 
white;,;09/15/17   ,   Jacob Kennedy ;,; $11.40   
;,; white&red   ;,; 09/15/17, Craig Chambers;,; 
$8.79 ;,; white&blue&red   ;,;09/15/17   , Peggy Bell;,; $8.65 ;,;blue   ;,; 09/15/17,   Kenneth Cunningham ;,;   $10.53;,;   green&blue   ;,; 
09/15/17   ,   Marvin Morgan;,;   $16.49;,; 
green&blue&red   ;,;   09/15/17 ,Marjorie Russell 
;,; $6.55 ;,;   green&blue&red;,;   09/15/17 ,
Israel Cummings;,;   $11.86   ;,;black;,;  
09/15/17,   June Doyle   ;,;   $22.29 ;,;  
black&yellow ;,;09/15/17 , Jaime Buchanan   ;,;   
$8.35;,;   white&black&yellow   ;,;   09/15/17,   
Rhonda Farmer;,;$2.91 ;,;   white&black&yellow   
;,;09/15/17, Darren Mckenzie ;,;$22.94;,;green 
;,;09/15/17,Rufus Malone;,;$4.70   ;,; green&yellow 
;,; 09/15/17   ,Hubert Miles;,;   $3.59   
;,;green&yellow&blue;,;   09/15/17   , Joseph Bridges  ;,;$5.66   ;,; green&yellow&purple&blue 
;,;   09/15/17 , Sergio Murphy   ;,;$17.51   ;,;   
black   ;,;   09/15/17 , Audrey Ferguson ;,; 
$5.54;,;black&blue   ;,;09/15/17 ,Edna Williams ;,; 
$17.13;,; black&blue;,;   09/15/17,   Randy Fleming;,;   $21.13 ;,;black ;,;09/15/17 ,Elisa Hart;,; $0.35   ;,; black&purple;,;   09/15/17   ,
Ernesto Hunt ;,; $13.91   ;,;   black&purple ;,;   
09/15/17,   Shannon Chavez   ;,;$19.26   ;,; 
yellow;,; 09/15/17   , Sammy Cain;,; $5.45;,;   
yellow&red ;,;09/15/17 ,   Steven Reeves ;,;$5.50   
;,;   yellow;,;   09/15/17, Ruben Jones   ;,; 
$14.56 ;,;   yellow&blue;,;09/15/17 , Essie Hansen;,;   $7.33   ;,;   yellow&blue&red
;,; 09/15/17   ,   Rene Hardy   ;,; $20.22   ;,; 
black ;,;   09/15/17 ,   Lucy Snyder   ;,; $8.67   
;,;black&red  ;,; 09/15/17 ,Dallas Obrien ;,;   
$8.31;,;   black&red ;,;   09/15/17,   Stacey Payne 
;,;   $15.70   ;,;   white&black&red ;,;09/15/17   
,   Tanya Cox   ;,;   $6.74   ;,;yellow   ;,; 
09/15/17 , Melody Moran ;,;   $30.84   
;,;yellow&black;,;   09/15/17 , Louise Becker   ;,; 
$12.31 ;,; green&yellow&black;,;   09/15/17 ,
Ryan Webster;,;$2.94 ;,; yellow ;,; 09/15/17 
,Justin Blake ;,; $22.46   ;,;white&yellow ;,;   
09/15/17,   Beverly Baldwin ;,;   $6.60;,;   
white&yellow&black ;,;09/15/17   ,   Dale Brady   
;,;   $6.27 ;,; yellow   ;,;09/15/17 ,Guadalupe Potter ;,;$21.12   ;,; yellow;,; 09/15/17   , 
Desiree Butler ;,;$2.10   ;,;white;,; 09/15/17  
,Sonja Barnett ;,; $14.22 ;,;white&black;,;   
09/15/17, Angelica Garza;,;$11.60;,;white&black   
;,;   09/15/17   ,   Jamie Welch   ;,; $25.27   ;,; 
white&black&red ;,;09/15/17   ,   Rex Hudson   
;,;$8.26;,;   purple;,; 09/15/17 ,   Nadine Gibbs 
;,;   $30.80 ;,;   purple&yellow   ;,; 09/15/17   , 
Hannah Pratt;,;   $22.61   ;,;   purple&yellow   
;,;09/15/17,Gayle Richards;,;$22.19 ;,; 
green&purple&yellow ;,;09/15/17   ,Stanley Holland 
;,; $7.47   ;,; red ;,; 09/15/17 , Anna Dean;,;$5.49 ;,; yellow&red ;,;   09/15/17   ,
Terrance Saunders ;,;   $23.70  ;,;green&yellow&red 
;,; 09/15/17 ,   Brandi Zimmerman ;,; $26.66 ;,; 
red   ;,;09/15/17 ,Guadalupe Freeman ;,; $25.95;,; 
green&red ;,;   09/15/17   ,Irving Patterson 
;,;$19.55 ;,; green&white&red ;,;   09/15/17 ,Karl Ross;,;   $15.68;,;   white ;,;   09/15/17 , Brandy Cortez ;,;$23.57;,;   white&red   ;,;09/15/17, 
Mamie Riley   ;,;$29.32;,; purple;,;09/15/17 ,Mike Thornton   ;,; $26.44 ;,;   purple   ;,; 09/15/17, 
Jamie Vaughn   ;,; $17.24;,;green ;,; 09/15/17   , 
Noah Day ;,;   $8.49   ;,;green   ;,;09/15/17   
,Josephine Keller ;,;$13.10 ;,;green;,;   09/15/17 ,   Tracey Wolfe;,;$20.39 ;,; red   ;,; 09/15/17 ,
Ignacio Parks;,;$14.70   ;,; white&red ;,;09/15/17 
, Beatrice Newman ;,;$22.45   ;,;white&purple&red 
;,;   09/15/17, Andre Norris   ;,;   $28.46   ;,;   
red;,;   09/15/17 ,   Albert Lewis ;,; $23.89;,;   
black&red;,; 09/15/17,   Javier Bailey   ;,;   
$24.49   ;,; black&red ;,; 09/15/17   , Everett Lyons ;,;$1.81;,;   black&red ;,; 09/15/17 ,   
Abraham Maxwell;,; $6.81   ;,;green;,;   09/15/17   
,   Traci Craig ;,;$0.65;,; green&yellow;,; 
09/15/17 , Jeffrey Jenkins   ;,;$26.45;,; 
green&yellow&blue   ;,;   09/15/17,   Merle Wilson 
;,;   $7.69 ;,; purple;,; 09/15/17,Janis Franklin   
;,;$8.74   ;,; purple&black   ;,;09/15/17 ,  
Leonard Guerrero ;,;   $1.86   ;,;yellow  
;,;09/15/17,Lana Sanchez;,;$14.75   ;,; yellow;,;   
09/15/17   ,Donna Ball ;,; $28.10  ;,; 
yellow&blue;,;   09/15/17   , Terrell Barber   ;,; 
$9.91   ;,; green ;,;09/15/17   ,Jody Flores;,; 
$16.34 ;,; green ;,;   09/15/17,   Daryl Herrera 
;,;$27.57;,; white;,;   09/15/17   , Miguel Mcguire;,;$5.25;,; white&blue   ;,;   09/15/17 ,   
Rogelio Gonzalez;,; $9.51;,;   white&black&blue   
;,;   09/15/17   ,   Lora Hammond ;,;$20.56 ;,; 
green;,;   09/15/17,Owen Ward;,; $21.64   ;,;   
green&yellow;,;09/15/17,Malcolm Morales ;,;   
$24.99   ;,;   green&yellow&black;,; 09/15/17 ,   
Eric Mcdaniel ;,;$29.70;,; green ;,; 09/15/17 
,Madeline Estrada;,;   $15.52;,;green;,;   09/15/17 
, Leticia Manning;,;$15.70 ;,; green&purple;,; 
09/15/17 ,   Mario Wallace ;,; $12.36 ;,;green ;,; 
09/15/17,Lewis Glover;,;   $13.66   ;,;   
green&white;,;09/15/17,   Gail Phelps   ;,;$30.52   
;,; green&white&blue   ;,; 09/15/17 , Myrtle Morris 
;,;   $22.66   ;,; green&white&blue;,;09/15/17"""

# ------------------------------------------------


# TODO: rename variables with intuitive names


daily_sales_replaced = daily_sales.replace(';,;', ';')
# print(daily_sales_replaced)
# print('\n\n\n')

daily_transactions = daily_sales_replaced.split(',')
# print(daily_transactions)
# print('\n\n\n')
daily_transactions_split = []
for i in daily_transactions:
    daily_transactions_split.append(i.split(';'))
# print(daily_transactions_split)
# print('\n\n\n')

transactions_clean = []
for i in daily_transactions_split:
    for j in i:
        transactions_clean.append(j.replace('\n', '').strip())
# print(transactions_clean)
# print('\n\n\n')


def sort(frequency, stuff):
    lst = []
    for i in range(frequency, len(stuff), 4):
        lst.append(stuff[i])
    return lst


customers = sort(0, transactions_clean)
print(customers)
sales = sort(1, transactions_clean)
print(sales)
threads_sold = sort(2, transactions_clean)
print(threads_sold)

sales_clean = []
total_sales = 0
for i in range(len(sales)):
    sales_clean.append(sales[i].strip('$'))
    total_sales += float(sales_clean[i])
# print(sales_clean)
# print('\n\n\n')
# print(total_sales)
# print('\n\n\n')

thread_sold_split = []
for i in threads_sold:
    if '&' in i:
        thread_sold_split.append(i.split('&'))
    else:
        thread_sold_split.append(i)
# print(thread_sold_split)
# print('\n\n\n')

thread_sold_split_all = []

for i in thread_sold_split:
    if type(i) == list:
        thread_sold_split_all.append(i)
    else:
        lst = []
        lst.append(i)
        thread_sold_split_all.append(lst)
# print(thread_sold_split_all)


def color_count(color):
    count = 0
    for i in thread_sold_split_all:
        for j in i:
            if j == color:
                count += 1
    return count


print(color_count('white'))

colors = ['red', 'yellow', 'green', 'white', 'black', 'blue', 'purple']

for i in colors:
    x = color_count(i)
    print('Thread Shed sold {0} threads of {1} thread today.'.format(x, i))
