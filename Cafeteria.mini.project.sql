create database cafeteria_db;
use cafeteria_db;
create table Coffee_sales (
Transaction_id varchar(100) primary key,
Item varchar(50),
Quantity int,
Price_Per_Unit decimal(10,2),
Total_Spent  decimal(10,2),
Payment_Method varchar(50),
Location varchar(50),
Transaction_Date date
);
select * from Coffee_sales limit 10;
-- Best Selling Item
select item,sum(total_spent) as total_sales from coffee_sales
group by item
order by item asc;
-- average price 
select count(Transaction_id)as total_transaction from coffee_sales;
select sum(Quantity) as total_quantity from coffee_sales;
select round(avg(total_spent)) as average_order_value from coffee_sales;
-- best selling itmes in Quanitity
select item, sum(Quantity) as Total_quantity from coffee_sales
group by item
order by Total_quantity desc;
-- High revenue generated item
select item,sum(total_spent) as High_revenue_item from coffee_sales
group by item
order by High_revenue_item desc;
-- payment meghtod
select Payment_Method, sum(total_spent) as payment_item from coffee_sales
group by Payment_Method
order by payment_item desc;
-- location wise sales
select Location, sum(total_spent) as Total_sales from coffee_sales
group by Location
order by Total_sales desc;
-- month wise sales
select month(Transaction_Date) as month,sum(total_spent) as monthly_sales from coffee_sales
group by month(Transaction_Date)
order by month desc;
-- year wise sales
select year(Transaction_Date) as month, sum(total_spent)as yearly_sales from coffee_sales
group by year(transaction_Date)
order by year(Transaction_Date) asc;
-- Daily sales 
select Transaction_Date, sum(total_spent)as Daily_sales from coffee_sales
group by Transaction_Date
order by Transaction_Date asc;
-- Revenue generate item
select item,sum(total_spent) as Revenue from coffee_sales
group by item
order by Revenue desc;




