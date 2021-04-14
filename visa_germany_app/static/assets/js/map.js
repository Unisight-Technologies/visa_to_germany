/**
 * ---------------------------------------
 * This demo was created using amCharts 4.
 *
 * For more information visit:
 * https://www.amcharts.com/
 *
 * Documentation is available at:
 * https://www.amcharts.com/docs/v4/
 * ---------------------------------------
 */

// Create map instance
// var chart = am4core.create("chartdiv", am4maps.MapChart);
//
// // Set map definition
// chart.geodata = am4geodata_worldLow;
//
// // Set projection
// chart.projection = new am4maps.projections.Miller();
//
// // Create map polygon series
// var polygonSeries = chart.series.push(new am4maps.MapPolygonSeries());
//
// // Exclude Antartica
// polygonSeries.exclude = ["AQ"];
//
// // Make map load polygon (like country names) data from GeoJSON
// polygonSeries.useGeodata = true;
//
// // Configure series
// var polygonTemplate = polygonSeries.mapPolygons.template;
// if( name == "Malta")
// {
//   polygonTemplate.tooltipHTML = '<b>{name}</b><br><a href="https://visatomalta.com">Visit us</a>';
//   console.log("Hi naitik !!!");
// }
// else {
//   polygonTemplate.tooltipHTML = '<b>{name}</b><br><a href="https:visato{name.urlEncode()}.pro">Visit us</a>';
//
// }
// polygonTemplate.fill = am4core.color("#74B266");
//
// // Set up tooltips
// polygonSeries.calculateVisualCenter = true;
// polygonTemplate.tooltipPosition = "fixed";
// polygonSeries.tooltip.label.interactionsEnabled = true;
// polygonSeries.tooltip.keepTargetHover = true;
//
// // Create hover state and set alternative fill color
// var hs = polygonTemplate.states.create("hover");
// hs.properties.fill = am4core.color("#367B25");



// <script>
// am4core.ready(function() {

// Themes begin
am4core.useTheme(am4themes_kelly);
am4core.useTheme(am4themes_animated);
// Themes end

// Create map instance
var chart = am4core.create("chartdiv", am4maps.MapChart);

// Set map definition
chart.geodata = am4geodata_worldLow;

// Set projection
chart.projection = new am4maps.projections.Miller();

// Create map polygon series
var polygonSeries = chart.series.push(new am4maps.MapPolygonSeries());

// Exclude Antartica
polygonSeries.exclude = ["AQ"];

// Make map load polygon (like country names) data from GeoJSON
polygonSeries.useGeodata = true;

// Configure series
var polygonTemplate = polygonSeries.mapPolygons.template;
polygonTemplate.tooltipText = "{name}";
polygonTemplate.polygon.fillOpacity = 0.6;
// polygonTemplate.fill = am4core.color("#ac943c");


// Create hover state and set alternative fill color
var hs = polygonTemplate.states.create("hover");
hs.properties.fill = chart.colors.getIndex(0);

// Add image series
var imageSeries = chart.series.push(new am4maps.MapImageSeries());
imageSeries.mapImages.template.propertyFields.longitude = "longitude";
imageSeries.mapImages.template.propertyFields.latitude = "latitude";
imageSeries.mapImages.template.tooltipText = "{title}";
imageSeries.mapImages.template.propertyFields.url = "url";

var circle = imageSeries.mapImages.template.createChild(am4core.Circle);
circle.radius = 4;
circle.propertyFields.fill = "color";

var circle2 = imageSeries.mapImages.template.createChild(am4core.Circle);
circle2.radius = 4;
circle2.propertyFields.fill = "color";


circle2.events.on("inited", function(event){
  animateBullet(event.target);
})


function animateBullet(circle) {
    var animation = circle.animate([{ property: "scale", from: 1, to: 5 }, { property: "opacity", from: 1, to: 0 }], 1000, am4core.ease.circleOut);
    animation.events.on("animationended", function(event){
      animateBullet(event.target.object);
    })
}

var colorSet = new am4core.ColorSet();


imageSeries.data = [ {
  "title": "Italy",
  "latitude": 41.2925,
  "longitude": 12.5736,
  "url":href="https://visatoitaly.com",
  "color":colorSet.next()
}, {
  "title": "Malta",
  "latitude": 35.917973,
  "longitude": 14.409943,
  "url":href="https://visatomalta.com",
  "color":colorSet.next()
}, {
  "title": "Spain",
  "latitude": 48.8567,
  "longitude": -3.7130,
  "url":href="https://visatospain.pro",
  "color":colorSet.next()
}, {
  "title": "Denmark",
  "latitude": 55.676098,
  "longitude": 12.568337,
  "url":href="https://visatodenmark.com",
  "color":colorSet.next()
}, {
  "title": "Portugal",
  "latitude": 39.5572 ,
  "longitude": -7.8537,
  "url":href="https://visatoportugal.pro",
  "color":colorSet.next()
}, {
  "title": "Greece",
  "latitude": 37.983810,
  "longitude": 23.727539,
  "url":href="https://visatogreece.pro",
  "color":colorSet.next()
}, {
  "title": "Cyprus",
  "latitude": 35.095192,
  "longitude": 33.203430,
  "url":href="https://visatocyprus.com",
  "color":colorSet.next()
}, {
  "title": "Ireland",
  "latitude": 53.41291,
  "longitude": -8.24389,
  "url":href="https://visatoireland.com",
  "color":colorSet.next()
}, {
  "title": "Canada",
  "latitude": 56.1303673,
  "longitude": -106.3467712,
  "url":href="https://visatocanada.pro",
  "color":colorSet.next()
}, {
  "title": "New Zealand",
  "latitude": -40.900557,
  "longitude": 174.885971,
  "url":href="https://visatonewzealand.com",
  "color":colorSet.next()
}, {
  "title": "Australia",
  "latitude": -33.868857,
  "longitude": 151.206079,
  "url":href="https://visatoaustralia.pro",
  "color":colorSet.next()
}, {
  "title": "Germany",
  "latitude": 51.165691,
  "longitude": 10.451526,
  "url":href="https://visatogermany.com",
  "color":colorSet.next()
}, {
  "title": "America",
  "latitude": 37.090240,
  "longitude": -95.712891,
  "url":href="https://visatoamerica.com",
  "color":colorSet.next()
},  ];



// }); // end am4core.ready()
// </script>
