<?php

// obteniendo los datos
$metrics 	= $_POST['metrics'];
$id 		= $_POST['id'];

// conectandose a la base de datos
$db_connect = mysql_connect("localhost", "nobody"); 
mysql_select_db("incc_tp1", $link) or die(mysql_error());

// insertando los datos en la base de date_offset_get()
$query 		= "INSERT INTO metrics VALUES('".$id."','".$metrics."')";
$result 	= mysql_query($query, $db_connect) or die(mysql_error()); 

if ($result) {
	echo "Metrics saved";
} else {
	echo "Error saving metrics";
}

?>
