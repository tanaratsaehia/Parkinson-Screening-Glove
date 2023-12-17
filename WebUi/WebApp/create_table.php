<?php
    include 'condb.php';
    $sql = "SELECT * FROM member";
    $result = mysqli_query($conn, $sql);
    while ($row = mysqli_fetch_array($result)) {
        $id = $row['id'];
    }mysqli_close($conn);
    $create = "CREATE TABLE `rec$id` (
        `id` int(3) NOT NULL AUTO_INCREMENT,
        `name` varchar(255) NOT NULL,
        `datetime` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
        `par_state` varchar(255) NOT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8";
    $result_create = mysqli_query($connect, $create);
    if($result_create){
        echo "<script>alert('success');</script>";
        echo "<script>window.location='index.php';</script>";
    }else{
        echo "kuy";
        echo "<script>alert('can't save data');</script>";
    }mysqli_close($connect);
?>