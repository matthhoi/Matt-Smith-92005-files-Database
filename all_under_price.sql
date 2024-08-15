-- SQLite
SELECT piece_id, piece_name, price, material, maker FROM pieces WHERE price <= 
250 AND purchase_status = 'Avalbile';