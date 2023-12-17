<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UserRecord</title>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
</head>
<body>
    <div class="container">
        <div class="h4 text-center alert alert-primary mb-2 mt-4" role="alert">User Record</div>
        <table class="table table-striped">
            <tr>
                <th>No</th>
                <th>Name</th>
                <th>Datetime</th>
                <th>State</th>
                <th>View</th>
                <th>Delete</th>
            </tr>
            <?php
                include 'condb.php';
                $id = "rec" . $_GET['id'];
                $id_page = $_GET['id'];
                $sql = "SELECT * FROM $id";
                $result = mysqli_query($conn, $sql);
                $count = 1;
                while ($row = mysqli_fetch_array($result)) {
            ?>
            <tr>
                <td><?= $count ?></td>
                <td><?= $row['name'] ?></td>
                <td><?= $row['datetime'] ?></td>
                <td><?= $row['par_state'] ?></td>
                <td><a href="show_table.php?table=<?=$id_page?>_<?=$row['id']?>&name=<?=$row['name']?>&datetime=<?=$row['datetime']?>" type="button" class="btn btn-info">view</a></td>
                <td><a href="delete.php?id=<?= $row['id'] ?>&table=<?= $id ?>&page=show_record.php&id_page=<?= $id_page?>" type="button" class="btn btn-danger" onclick="del(this.href); return false;">Delete</a></td>
            </tr>
            <?php
                $count += 1;
                }
                mysqli_close($conn);
            ?>
        </table>
        <a href="index.php" type="button" class="btn btn-danger">Back</a>
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