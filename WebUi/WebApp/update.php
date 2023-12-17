<?php
    include 'condb.php';
    $id = $_POST['idmem'];
    $fname = $_POST['fname'];
    $lname = $_POST['lname'];
    $tel = $_POST['telephone'];
    $sql = "UPDATE member SET firstname='$fname', lastname='$lname', phone='$tel' WHERE id='$id'";
    $result = mysqli_query($conn, $sql);
    if($result){
        echo "<script>alert('UpdateSuccess');</script>";
        echo "<script>window.location='index.php';</script>";
    }else{
        echo "<script>alert('can't update data');</script>";
    }mysqli_close($conn);
?>