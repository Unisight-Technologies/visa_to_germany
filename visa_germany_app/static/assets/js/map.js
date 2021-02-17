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
if( name == "Malta")
{
  polygonTemplate.tooltipHTML = '<b>{name}</b><br><a href="https://visatomalta.com">Visit us</a>';
  console.log("Hi naitik !!!");
}
else {
  polygonTemplate.tooltipHTML = '<b>{name}</b><br><a href="https:visato{name.urlEncode()}.pro">Visit us</a>';

}
polygonTemplate.fill = am4core.color("#74B266");

// Set up tooltips
polygonSeries.calculateVisualCenter = true;
polygonTemplate.tooltipPosition = "fixed";
polygonSeries.tooltip.label.interactionsEnabled = true;
polygonSeries.tooltip.keepTargetHover = true;

// Create hover state and set alternative fill color
var hs = polygonTemplate.states.create("hover");
hs.properties.fill = am4core.color("#367B25");
