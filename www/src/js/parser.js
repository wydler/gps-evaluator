var map;
var marker;
var circle;
var latlng;

function initialize() {
  var color_circle = "#0033FF";
  var color_path = "#0033FF"

  map = new google.maps.Map(
    document.getElementById("map_canvas"), {
      zoom: 18,
      center: new google.maps.LatLng(47.8142, 9.6523),
      mapTypeId: google.maps.MapTypeId.HYBRID
  });

  marker = new google.maps.Marker({
    map: map,
    animation: google.maps.Animation.DROP,
  });

  circle = new google.maps.Circle({
    strokeColor: color_circle,
    strokeOpacity: 0.5,
    strokeWeight: 1,
    fillColor: color_circle,
    fillOpacity: 0.25,
    map: map,
    center: new google.maps.LatLng( 50, 50 ),
    radius: 15
  });

  path = new Array();
  polyline = new google.maps.Polyline({
    map: map,
    strokeColor: color_path,
    strokeOpacity: 1,
    strokeWeight: 3,
  });

  $('#checkbox_path').click(function() {
    var satisfied = $('#checkbox_path:checked').val();
    if (satisfied != undefined) 
      polyline.setVisible(true);
    else 
      polyline.setVisible(false);
  });

  $('#checkbox_radius').click(function() {
    var satisfied = $('#checkbox_radius:checked').val();
    if (satisfied != undefined) 
      circle.setVisible(true);
    else 
      circle.setVisible(false);
  });

  $('#cp_circle').ColorPicker({
    onShow: function (colpkr) {
      $(colpkr).fadeIn(500);
      return false;
    },
    onBeforeShow: function () {
      $(this).ColorPickerSetColor(color_circle);
    },
    onHide: function (colpkr) {
      $(colpkr).fadeOut(500);
      return false;
    },
    onChange: function (hsb, hex, rgb) {
      color_circle = '#' + hex;
      circle.setOptions({
        strokeColor: color_circle,
        fillColor: color_circle,
      });
    },
    onSubmit: function (hsb, hex, rgb) {
      color_circle = '#' + hex;
      circle.setOptions({
        strokeColor: color_circle,
        fillColor: color_circle,
      });
    }
  });

  $('#cp_path').ColorPicker({
    onShow: function (colpkr) {
      $(colpkr).fadeIn(500);
      return false;
    },
    onBeforeShow: function () {
      $(this).ColorPickerSetColor(color_path);
    },
    onHide: function (colpkr) {
      $(colpkr).fadeOut(500);
      return false;
    },
    onChange: function (hsb, hex, rgb) {
      color_path = '#' + hex;
      polyline.setOptions({
        strokeColor: color_path,
      });
    },
    onSubmit: function (hsb, hex, rgb) {
      color_path = '#' + hex;
      polyline.setOptions({
        strokeColor: color_path,
      });
    }
  });
}

function update() {
  $.getJSON('data.json', function(data) {
    $("#data_date").html(data.date);
    $("#data_time").html(data.time + " UTC");

    if (data.latitude[0] != 0) {
      $("#data_lat").html(data.latitude[0] + "' " + data.latitude[1]);
    }
    if (data.longitude[0] != 0) {
      $("#data_lng").html(data.longitude[0] + "' " + data.longitude[1]);
    }
    if (data.altitude[0] != 0) {
      $("#data_alt").html(data.altitude[0] + " " + data.altitude[1]);
    }

    $("#data_fix").html(data.fix);
    switch (data.fix) {
      case "1":
        $("#data_fix").html("no fix");
        break;
      case "2":
        $("#data_fix").html("2D fix");
        break;
      case "3":
        $("#data_fix").html("3D fix");
        break;
    }
    $("#data_quality").html(data.quality);
    switch (data.quality) {
      case "0":
        $("#data_quality").html("invalid");
        break;
      case "1":
        $("#data_quality").html("GPS fix (SPS)");
        break;
      case "2":
        $("#data_quality").html("DGPS fix");
        break;
      case "3":
        $("#data_quality").html("PPS fix");
        break;
      case "4":
        $("#data_quality").html("Real Time Kinematic");
        break;
      case "5":
        $("#data_quality").html("Float RTK");
        break;
      case "6":
        $("#data_quality").html("estimated");
        break;
      case "7":
        $("#data_quality").html("Manual input mode");
        break;
      case "8":
        $("#data_quality").html("Simulation mode");
        break;
    }
    $("#data_satellites").html(data.satellites);

    $("#data_pdop").html(data.pdop);
    $("#data_hdop").html(data.hdop);
    $("#data_vdop").html(data.vdop);

    if (data.latitude[0] != 0 && data.longitude[0] != 0) {
      latlng = new google.maps.LatLng(data.latitude[0], data.longitude[0]);
      map.panTo(latlng);
      marker.setPosition(latlng);
    }
    circle.setCenter(latlng);
    circle.setRadius(6*data.pdop);

    if (path.length > 100)
      path.shift();

    path.push(latlng);

    polyline.setPath(path);
  })
  .error(function(request, error) { console.log(error); });
}