<?php
    include 'condb.php';
    $f_name = $_POST['fname'];
    $l_name = $_POST['lname'];
    $tel = $_POST['telephone'];
    $insert = "INSERT INTO member(firstname, lastname, phone) VALUES('$f_name', '$l_name', '$tel')";
    $result_insert = mysqli_query($conn, $insert);
    if($result_insert){ 
        echo "<script>window.location='create_table.php';</script>";
    }else{
        echo "<script>alert('can't save data');</script>";
    }mysqli_close($conn);
?>