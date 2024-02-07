<?php
// Database configuration
$servername = "localhost";
$user = "root";
$pswd = "";
$database = "siboga";

// Create a connection
$kon = new mysqli($servername, $user, $pswd, $database);

// Check the connection
if ($kon->connect_error) {
    die("Connection failed: " . $kon->connect_error);
}

// Set UTF-8 character set (optional, depending on your needs)
$kon->set_charset("utf8");

// Now, $conn is the mysqli connection object that you can use for database operations
?>
