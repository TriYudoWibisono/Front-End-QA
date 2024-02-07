    <!-- table advanced -->
    <!-- Bootstrap Color Picker -->
    <link rel="stylesheet" href="../../../../../plugins/bootstrap-colorpicker/css/bootstrap-colorpicker.min.css">
    <!-- Select2 -->
    <link rel="stylesheet" href="../../../../../plugins/select2-bootstrap4-theme/select2-bootstrap4.min.css">
    <!-- Bootstrap4 Duallistbox -->
    <link rel="stylesheet" href="../../../../../plugins/bootstrap4-duallistbox/bootstrap-duallistbox.min.css">
    <!-- BS Stepper -->
    <link rel="stylesheet" href="../../../../../plugins/bs-stepper/css/bs-stepper.min.css">
    <!-- dropzonejs -->
    <link rel="stylesheet" href="../../../../../plugins/dropzone/min/dropzone.min.css">


    <!-- Google Font: Source Sans Pro -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="../../../../../plugins/fontawesome-free/css/all.min.css">
    <!-- Ekko Lightbox -->
    <link rel="stylesheet" href="../../../../../plugins/ekko-lightbox/ekko-lightbox.css">
    <!-- Theme style -->
    <link rel="stylesheet" href="../../../../../dist/css/adminlte.min.css">


    <!-- setting css filter menu -->
    <style>
    .item_filter_menu {
        display: none;
    }

    .active_filter_menu {
        display: block;
    }
    </style>


<div class="container-fluid mt-3">
    <div class="row">
        <!-- left column -->
        <div class="col-md-12">
            <!-- form start -->
            <form>
                <!-- SELECT2 EXAMPLE -->
                <div class="card card-default">
                    <div class="card-header">
                        <h3 class="card-title"><strong>KEGIATAN PENALARAN DAN KEILMUAN</strong></h3>

                        <div class="card-tools">
                        <button type="button" class="btn btn-tool" data-card-widget="collapse">
                            <i class="fas fa-minus"></i>
                        </button>
                        <button type="button" class="btn btn-tool" data-card-widget="remove">
                            <i class="fas fa-times"></i>
                        </button>
                        </div>
                    </div>
                    <!-- /.card-header -->
                    <div class="card-body"> 
                        <div class="row">
                            <div class="col-md-9">
                                <div>
                                <div class="form-group">
                                    <label>Jenis Kegiatan</label>
                                    <select class="form-control select2" style="width: 100%;" id="pilihjenis" onchange="filterItems()">
                                        <option selected="selected">- pilih -</option>
                                        <option value="kegiatan">Kegiatan Ilmiah</option>
                                        <option value="publikasi">Publikasi Ilmiah</option>
                                        <option value="populer">Publikasi Populer</option>
                                        <option value="penghargaan">Penghargaan Lomba Kegiatan Akademik/Ilmiah</option>
                                        <option value="lomba">Kepesertaan Lomba Kegiatan Akademik/Ilmiah</option>
                                        <option value="nonlomba">Kepesertaan Nonlomba Kegiatan Akademik/Ilmiah</option>
                                    </select>
                                </div>
                                <!-- /.form-group -->
                                </div>
                                <div>
                                    <div class="form-group item_filter_menu" data-category="kegiatan publikasi populer penghargaan lomba nonlomba">
                                        <label for="nama_kegiatan">Nama Kegiatan</label>
                                        <input type="email" class="form-control" id="nama_kegiatan" placeholder="Masukan Nama Kegiatan">
                                    </div>
                                    <!-- /.form-group -->

                                    <div class="form-group item_filter_menu" data-category="kegiatan penghargaan lomba nonlomba">
                                        <label>Skala Kegiatan</label>
                                        <select class="form-control select2" style="width: 100%;">
                                            <option selected="selected">- pilih -</option>
                                            <option value="menu1">Internasional</option>
                                            <option value="menu1">Nasional</option>
                                            <option value="menu1">Regional</option>
                                            <option value="menu1">STIE YKPN</option>
                                            <option value="menu1">Program Studi</option>
                                        </select>
                                    </div>
                                    <!-- /.form-group -->
                                    <div class="form-group item_filter_menu" data-category="publikasi populer">
                                        <label>Skala Kegiatan</label>
                                        <select class="form-control select2" style="width: 100%;">
                                            <option selected="selected">- pilih -</option>
                                            <option value="menu1">Internasional</option>
                                            <option value="menu1">Nasional</option>
                                        </select>
                                    </div>
                                    <!-- /.form-group -->

                                    <div class="form-group item_filter_menu" data-category="kegiatan">
                                        <label>Kedudukan / Posisi</label>
                                        <select class="form-control select2" style="width: 100%;">
                                            <option selected="selected">- pilih -</option>
                                            <option value="menu1">Pembicara</option>
                                            <option value="menu1">Moderator</option>
                                            <option value="menu1">Peserta</option>
                                        </select>
                                    </div>
                                    <!-- /.form-group -->
                                    <div class="form-group item_filter_menu" data-category="publikasi populer">
                                        <label>Kedudukan / Posisi</label>
                                        <select class="form-control select2" style="width: 100%;">
                                            <option selected="selected">- pilih -</option>
                                            <option value="menu1">Penulis Pertama</option>
                                            <option value="menu1">Bukan Penulis Pertama</option>
                                        </select>
                                    </div>
                                    <!-- /.form-group -->
                                    <div class="form-group item_filter_menu" data-category="penghargaan">
                                        <label>Kedudukan / Posisi</label>
                                        <select class="form-control select2" style="width: 100%;">
                                            <option selected="selected">- pilih -</option>
                                            <option value="menu1">Juara 1</option>
                                            <option value="menu1">Juara 2</option>
                                            <option value="menu1">Juara 3</option>
                                            <option value="menu1">Favorit/Lainnya</option>
                                        </select>
                                    </div>
                                    <!-- /.form-group -->

                                    <div class="form-group" data-category="">
                                        <label for="bukti">Bukti</label>
                                        <div class="input-group">
                                        <div class="custom-file">
                                            <input type="file" class="custom-file-input" id="bukti">
                                            <label class="custom-file-label" for="exampleInputFile">Upload Sertifikat</label>
                                        </div>
                                        </div>
                                    </div>
                                    <!-- /.form-group -->
                                    <div class="form-group">
                                        <label>Bukti</label>
                                        <select class="form-control" id="buktiFilter" style="width: 100%;">
                                            <option selected="selected">- pilih -</option>
                                            <option value="menu1">Upload File</option>
                                            <option value="menu1">Link</option>
                                        </select>
                                    </div>
                                    <!-- /.form-group -->
                                </div>
                            </div>        
                            <!-- /.col -->
                        </div>
                        <!-- /.row -->
                    </div>
                    <!-- /.card-body -->

                </div>
                <!-- /.card -->

                    <div class="card-footer">
                        <button type="submit" class="btn btn-primary">Submit</button>
                    </div>
            </form>
        </div><!-- /.class -->
    </div><!-- /.row -->
</div><!-- /.container-fluid -->


<!-- tabel advanced -->
<!-- Bootstrap4 Duallistbox -->
<script src="../../../../../plugins/bootstrap4-duallistbox/jquery.bootstrap-duallistbox.min.js"></script>
<!-- InputMask -->
<script src="../../../../../plugins/moment/moment.min.js"></script>
<script src="../../../../../plugins/inputmask/jquery.inputmask.min.js"></script>
<!-- date-range-picker -->
<script src="../../../../../plugins/daterangepicker/daterangepicker.js"></script>
<!-- bootstrap color picker -->
<script src="../../../../../plugins/bootstrap-colorpicker/js/bootstrap-colorpicker.min.js"></script>
<!-- Tempusdominus Bootstrap 4 -->
<script src="../../../../../plugins/tempusdominus-bootstrap-4/js/tempusdominus-bootstrap-4.min.js"></script>
<!-- Bootstrap Switch -->
<script src="../../../../../plugins/bootstrap-switch/js/bootstrap-switch.min.js"></script>
<!-- BS-Stepper -->
<script src="../../../../../plugins/bs-stepper/js/bs-stepper.min.js"></script>
<!-- dropzonejs -->
<script src="../../../../../plugins/dropzone/min/dropzone.min.js"></script>
<!-- script penting tabel advanced -->
<script>
    $(function () {
        //Initialize Select2 Elements
        $('.select2').select2()

        //Initialize Select2 Elements
        $('.select2bs4').select2({
        theme: 'bootstrap4'
        })

        //Datemask dd/mm/yyyy
        $('#datemask').inputmask('dd/mm/yyyy', { 'placeholder': 'dd/mm/yyyy' })
        //Datemask2 mm/dd/yyyy
        $('#datemask2').inputmask('mm/dd/yyyy', { 'placeholder': 'mm/dd/yyyy' })
        //Money Euro
        $('[data-mask]').inputmask()

        //Date picker
        $('#reservationdate').datetimepicker({
            format: 'L'
        });

        //Date and time picker
        $('#reservationdatetime').datetimepicker({ icons: { time: 'far fa-clock' } });

        //Date range picker
        $('#reservation').daterangepicker()
        //Date range picker with time picker
        $('#reservationtime').daterangepicker({
        timePicker: true,
        timePickerIncrement: 30,
        locale: {
            format: 'MM/DD/YYYY hh:mm A'
        }
        })
        //Date range as a button
        $('#daterange-btn').daterangepicker(
        {
            ranges   : {
            'Today'       : [moment(), moment()],
            'Yesterday'   : [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
            'Last 7 Days' : [moment().subtract(6, 'days'), moment()],
            'Last 30 Days': [moment().subtract(29, 'days'), moment()],
            'This Month'  : [moment().startOf('month'), moment().endOf('month')],
            'Last Month'  : [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
            },
            startDate: moment().subtract(29, 'days'),
            endDate  : moment()
        },
        function (start, end) {
            $('#reportrange span').html(start.format('MMMM D, YYYY') + ' - ' + end.format('MMMM D, YYYY'))
        }
        )

        //Timepicker
        $('#timepicker').datetimepicker({
        format: 'LT'
        })

        //Bootstrap Duallistbox
        $('.duallistbox').bootstrapDualListbox()

        //Colorpicker
        $('.my-colorpicker1').colorpicker()
        //color picker with addon
        $('.my-colorpicker2').colorpicker()

        $('.my-colorpicker2').on('colorpickerChange', function(event) {
        $('.my-colorpicker2 .fa-square').css('color', event.color.toString());
        })

        $("input[data-bootstrap-switch]").each(function(){
        $(this).bootstrapSwitch('state', $(this).prop('checked'));
        })

    })
    // BS-Stepper Init
    document.addEventListener('DOMContentLoaded', function () {
        window.stepper = new Stepper(document.querySelector('.bs-stepper'))
    })

    // DropzoneJS Demo Code Start
    Dropzone.autoDiscover = false

    // Get the template HTML and remove it from the doumenthe template HTML and remove it from the doument
    var previewTemplate = previewNode.parentNode.innerHTML
    previewNode.parentNode.removeChild(previewNode)

    var myDropzone = new Dropzone(document.body, { // Make the whole body a dropzone
        url: "/target-url", // Set the url
        thumbnailWidth: 80,
        thumbnailHeight: 80,
        parallelUploads: 20,
        previewTemplate: previewTemplate,
        autoQueue: false, // Make sure the files aren't queued until manually added
        previewsContainer: "#previews", // Define the container to display the previews
        clickable: ".fileinput-button" // Define the element that should be used as click trigger to select files.
    })

    myDropzone.on("addedfile", function(file) {
        // Hookup the start button
        file.previewElement.querySelector(".start").onclick = function() { myDropzone.enqueueFile(file) }
    })

    // Update the total progress bar
    myDropzone.on("totaluploadprogress", function(progress) {
        document.querySelector("#total-progress .progress-bar").style.width = progress + "%"
    })

    myDropzone.on("sending", function(file) {
        // Show the total progress bar when upload starts
        document.querySelector("#total-progress").style.opacity = "1"
        // And disable the start button
        file.previewElement.querySelector(".start").setAttribute("disabled", "disabled")
    })

    // Hide the total progress bar when nothing's uploading anymore
    myDropzone.on("queuecomplete", function(progress) {
        document.querySelector("#total-progress").style.opacity = "0"
    })

    // Setup the buttons for all transfers
    // The "add files" button doesn't need to be setup because the config
    // `clickable` has already been specified.
    document.querySelector("#actions .start").onclick = function() {
        myDropzone.enqueueFiles(myDropzone.getFilesWithStatus(Dropzone.ADDED))
    }
    document.querySelector("#actions .cancel").onclick = function() {
        myDropzone.removeAllFiles(true)
    }
    // DropzoneJS Demo Code End
</script>


<!-- setting JS filter menu -->
<script>
    function filterItems() {
    const categoryFilter = document.getElementById('pilihjenis');
    const selectedCategory = pilihjenis.value;

    const items = document.getElementsByClassName('item_filter_menu');
    for (const item of items) {
        const itemCategories = item.getAttribute('data-category').split(' ');

        if (selectedCategory === 'all' || itemCategories.includes(selectedCategory)) {
        item.classList.add('active_filter_menu');
        } else {
        item.classList.remove('active_filter_menu');
        }
    }
    }
</script>