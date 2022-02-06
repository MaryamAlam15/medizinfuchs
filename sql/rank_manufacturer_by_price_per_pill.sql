select
    DISTINCT manufacturer,
             name,
             dosage,
             dosage_unit,
             number_of_pills,
             quantity_unit,
             low_price,
             price_per_unit,
             product
from products
WHERE dosage IS NOT ''
group by product, dosage, number_of_pills
order by price_per_unit