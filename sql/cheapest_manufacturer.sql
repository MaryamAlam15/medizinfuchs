select
    product,
    manufacturer,
    name,
    dosage,
    dosage_unit,
    price,
    quantity,
    price_per_unit
from
    (
        select
            product,
            manufacturer,
            name,
            dosage,
            dosage_unit,
            low_price as price,
            number_of_pills as quantity,
            price_per_unit,
            row_number() over (partition by product, dosage, number_of_pills order by low_price) as cheapest_manufacturer
        from products
        group by product, dosage, number_of_pills
    )
where cheapest_manufacturer = 1