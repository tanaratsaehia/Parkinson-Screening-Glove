<?php 
    include 'condb.php';
    $id = $_GET['id'];
    $id_page = $_GET['id_page'];
    $table = $_GET['table'];
    $page = $_GET['page'];
    $table_member = $_GET['table_member'];
    $sql = "DELETE FROM $table WHERE id=$id";
    mysqli_query($conn, "DROP TABLE $table_member");
    if(mysqli_query($conn, $sql)){
        //echo "<script>alert('Delete Success');</script>";
        echo "<script>window.location='" . $page . "?id=" . $id_page . "';</script>";
    }else{
        echo"Error : " . $sql . "<br>" . mysqli_error($conn);
    }mysqli_close($conn);
?>