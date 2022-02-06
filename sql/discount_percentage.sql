select p.product,
       p.dosage,
       p.dosage_unit,
       p.number_of_pills,
       p.quantity_unit,
       m.most_expensive_item,
       p.low_price,
       ((m.most_expensive_item - p.low_price) / m.most_expensive_item) * 100 as discount_percentage
from (
         select distinct max(low_price)
                             over (partition by product, dosage, number_of_pills order by low_price desc) as most_expensive_item,
                 product,
                         dosage,
                         number_of_pills
         from products
     ) m,
     products p
where m.product = p.product
  and m.dosage = p.dosage
  and m.number_of_pills = p.number_of_pills