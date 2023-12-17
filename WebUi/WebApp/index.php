<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HomePage</title>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
</head>

<body>
    
    <div class="container">
    <div class="h4 text-center alert alert-primary mb-2 mt-4" role="alert">HomePage</div>
        <table class="table table-striped">
            <tr>
                <th>ID</th>
                <th>FirstName</th>
                <th>LastName</th>
                <th>Phone</th>
                <th>View</th>
                <th>Edit</th>
                <th>Delete</th>
            </tr>
            <?php
            include 'condb.php';
            $sql = "SELECT * FROM member";  
            $result = mysqli_query($conn, $sql);
            while ($row = mysqli_fetch_array($result)) {
            ?>
            <tr>
                <td><?= $row["id"] ?></td>
                <td><?= $row["firstname"] ?></td>
                <td><?= $row["lastname"] ?></td>
                <td><?= $row["phone"] ?></td>
                <td><a href="show_record.php?id=<?= $row["id"] ?>" type="button" class="btn btn-info">ShowRecord</a></td>
                <td><a href="edit.php?id=<?= $row["id"] ?>" type="button" class="btn btn-warning">Edit</a></td>
                <td><a href="delete.php?id=<?= $row["id"] ?>&table=member&table_member=rec<?=$row["id"]?>&page=index.php" type="button" class="btn btn-danger" onclick="del(this.href); return false;">Delete</a></td>
            </tr>
            <?php
            }
            mysqli_close($conn);
            ?>
        </table>
        <a type="button" class="btn btn-success mb-2" href="add.php">Add+</a>
    </div>
</body>
</html>

<script>
    function del(homepage){
        let agree = confirm("Confirm to delete");
        if(agree){
            window.location = homepage;
        }
    }
</script>