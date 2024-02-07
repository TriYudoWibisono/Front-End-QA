<?php
    session_start();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>AdminLTE 3 | Dashboard</title>

    <!-- Google Font: Source Sans Pro -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="../../../../plugins/fontawesome-free/css/all.min.css">
    <!-- Ionicons -->
    <link rel="stylesheet" href="https://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css">
    
    <!-- Tempusdominus Bootstrap 4 -->
    <link rel="stylesheet" href="../../../../plugins/tempusdominus-bootstrap-4/css/tempusdominus-bootstrap-4.min.css">
    <!-- iCheck -->
    <link rel="stylesheet" href="../../../../plugins/icheck-bootstrap/icheck-bootstrap.min.css">
    <!-- JQVMap -->
    <link rel="stylesheet" href="../../../../plugins/jqvmap/jqvmap.min.css">
    <!-- Theme style -->
    <link rel="stylesheet" href="../../../../dist/css/adminlte.min.css">
    <!-- overlayScrollbars -->
    <link rel="stylesheet" href="../../../../plugins/overlayScrollbars/css/OverlayScrollbars.min.css">
    <!-- Daterange picker -->
    <link rel="stylesheet" href="../../../../plugins/daterangepicker/daterangepicker.css">
    <!-- summernote -->
    <link rel="stylesheet" href="../../../../plugins/summernote/summernote-bs4.min.css">
 

    <!-- enhanced -->
    <!-- Select2 -->
    <link rel="stylesheet" href="../../../../plugins/select2/css/select2.min.css">

    <!-- Theme style -->
    <link rel="stylesheet" href="../../../../dist/css/adminlte.min.css">

    <!-- css custom -->
    <link rel="stylesheet" href="../../CSS/style.css">


    <!-- table advanced -->
    <!-- Bootstrap Color Picker -->
    <link rel="stylesheet" href="../../../../plugins/bootstrap-colorpicker/css/bootstrap-colorpicker.min.css">
    <!-- Select2 -->
    <link rel="stylesheet" href="../../../../plugins/select2-bootstrap4-theme/select2-bootstrap4.min.css">
    <!-- Bootstrap4 Duallistbox -->
    <link rel="stylesheet" href="../../../../plugins/bootstrap4-duallistbox/bootstrap-duallistbox.min.css">
    <!-- BS Stepper -->
    <link rel="stylesheet" href="../../../../plugins/bs-stepper/css/bs-stepper.min.css">
    <!-- dropzonejs -->
    <link rel="stylesheet" href="../../../../plugins/dropzone/min/dropzone.min.css">



    <!-- setting css filter menu -->
    <style>
    .item_filter_menu {
      display: none;
    } 

    .active_filter_menu {
      display: block;
    }
    </style>

</head>
<body class="hold-transition sidebar-mini layout-fixed">
    <div class="wrapper">

    <!-- Preloader -->
    <div class="preloader flex-column justify-content-center align-items-center">
        <img class="animation__shake" src="../../../../dist/img/AdminLTELogo.png" alt="AdminLTELogo" height="60" width="60">
    </div>

    <!-- Navbar -->
    <?php include "../../include_views/navbar.php";?> 
    <!-- Navbar -->
            
    <!-- Sidebar -->
    <?php
        include "../../include_views/sidebar.php"; 
    ?>
    <!-- Sidebar -->

        <!-- Content Wrapper. Contains page content -->
        <div class="content-wrapper">
            <!-- Main content -->
            <section class="content mt-1 mb-3">
                <div class="container-fluid">
                    <div class="row">
                    <div class="col-12">

                        <div class="card">
                        <!-- /.card-header -->
                        <div class="card-body">
                            <div class="container-fluid">
                                <form action="enhanced-results.html">
                                    <div class="row">
                                        <div class="col-md-10">
                                            <div class="row">
                                                <div class="col-4">
                                                    <div class="form-group">
                                                        <label>Pilih Menu : </label>
                                                        <select class="select2" style="width: 100%;" name="" id="entry">
                                                            <option selected value="wajib">Kegiatan Wajib</option>
                                                            <option value="penalaran">Kegiatan Penalaran Dan Keilmuan</option>
                                                            <option value="minat">Kegiatan Minat Dan Bakat</option>
                                                            <option value="organisasi">Kegiatan Organisasi Dan Kepemimpinan</option>
                                                            <option value="pengabdian">Kegiatan Pengabdian Kepada Masyarakat Dan Kewirausahaan</option>
                                                        </select>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </form>
                            </div>

                            <div id="content"></div>
                        
                        </div>
                        <!-- /.card-body -->
                        </div>
                        <!-- /.card -->
                    </div>
                    <!-- /.col -->
                    </div>
                    <!-- /.row -->
                </div>
                <!-- /.container-fluid -->
            </section>
            <!-- /.content -->
        </div>
        <!-- /.content-wrapper -->
    
        <!-- footer -->
        <?php
            include "../../include_views/footer.php";
        ?>
        <!-- footer -->

        <!-- Control Sidebar -->
        <aside class="control-sidebar control-sidebar-dark">
            <!-- Control sidebar content goes here -->
        </aside>
        <!-- /.control-sidebar -->
    </div>
    <!-- ./wrapper -->


<!-- jQuery -->
<script src="../../../../plugins/jquery/jquery.min.js"></script>
<!-- jQuery UI 1.11.4 -->
<script src="../../../../plugins/jquery-ui/jquery-ui.min.js"></script>
<!-- Resolve conflict in jQuery UI tooltip with Bootstrap tooltip -->
<script>
    $.widget.bridge('uibutton', $.ui.button)
</script>
<!-- Bootstrap 4 -->
<script src="../../../../plugins/bootstrap/js/bootstrap.bundle.min.js"></script>

<!-- Select2 -->
<script src="../../../../plugins/select2/js/select2.full.min.js"></script>
<!-- AdminLTE App -->
<script src="../../../../dist/js/adminlte.min.js"></script>
<!-- AdminLTE for demo purposes -->
<script src="../../../../dist/js/demo.js"></script>
<script>
    $(function () {
        $('.select2').select2()
    });
</script>

<!-- tabel advanced -->
<!-- Bootstrap4 Duallistbox -->
<script src="../../../../plugins/bootstrap4-duallistbox/jquery.bootstrap-duallistbox.min.js"></script>
<!-- InputMask -->
<script src="../../../../plugins/moment/moment.min.js"></script>
<script src="../../../../plugins/inputmask/jquery.inputmask.min.js"></script>
<!-- date-range-picker -->
<script src="../../../../plugins/daterangepicker/daterangepicker.js"></script>
<!-- bootstrap color picker -->
<script src="../../../../plugins/bootstrap-colorpicker/js/bootstrap-colorpicker.min.js"></script>
<!-- Tempusdominus Bootstrap 4 -->
<script src="../../../../plugins/tempusdominus-bootstrap-4/js/tempusdominus-bootstrap-4.min.js"></script>
<!-- Bootstrap Switch -->
<script src="../../../../plugins/bootstrap-switch/js/bootstrap-switch.min.js"></script>
<!-- BS-Stepper -->
<script src="../../../../plugins/bs-stepper/js/bs-stepper.min.js"></script>
<!-- dropzonejs -->
<script src="../../../../plugins/dropzone/min/dropzone.min.js"></script>


<!-- JS filter menu input -->
<!-- Ekko Lightbox -->
<script src="../../../../plugins/ekko-lightbox/ekko-lightbox.min.js"></script>
<!-- Filterizr-->
<script src="../../../../plugins/filterizr/jquery.filterizr.min.js"></script>

<!-- load javascript select -->
<script>
    let page = $('#entry').val();
    loadPage(page);

    $(document).on("change", "#entry", function(){
        page = $(this).val();
        // console.log(page);
        loadPage(page);
        
    });

    function loadPage(page) {
        switch(page){
            case "wajib":
                $("#content").load("input/wajib.php");
                break;
            case "penalaran":
                $("#content").load("input/penalaran.php");
                break;
            case "minat":
                $("#content").load("input/minat.php");
                break;
            case "organisasi":
                $("#content").load("input/organisasi.php");
                break;
            case "pengabdian":
                $("#content").load("input/pengabdian.php");
                break;
            default:
                break;
        }
    }
</script>


<!-- setting JS filter menu -->
<script>
    function filterItems() {
        const categoryFilter = document.getElementById('pilihjenis');
        const selectedCategory = categoryFilter.value;

        const items = document.getElementsByClassName('"item_filter_menu');
        for (const item of items) {
        const itemCategory = item.getAttribute('data-category');
        if (selectedCategory === 'all' || itemCategory === selectedCategory) {
            item.classList.add('active_filter_menu');
        } else {
            item.classList.remove('active_filter_menu');
        }
        }
    }
</script>

</body>
</html>
