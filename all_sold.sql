-- SQLite
SELECT pieces.piece_id, pieces.price, pieces.piece_name, customers.first_name, 
customers.postal_address FROM pieces JOIN customer_piece, customers ON 
customer_piece.piece_id = pieces.piece_id AND customer_piece.customer_id = 
customers.customer_id;