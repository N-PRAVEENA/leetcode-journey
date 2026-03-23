SELECT
    s.user_id,
    ROUND(coalesce(
        AVG(
            CASE 
                WHEN c.action = 'confirmed' THEN 1.00
                WHEN c.action = 'timeout' THEN 0.00

            END
        ),0),
        2
    ) confirmation_rate
FROM
    Signups s
LEFT JOIN
    Confirmations c
    ON
    s.user_id = c.user_id
GROUP BY
    s.user_id