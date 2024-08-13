-- SQLite
SELECT pieces.piece_id, pieces.price, pieces.piece_name, customers.first_name, 
customers.last_name, customers.postal_address, customers.town, 
customers.postal_code FROM pieces JOIN customer_piece, customers ON 
customer_piece.piece_id = pieces.piece_id AND customer_piece.customer_id = 
customers.customer_id;