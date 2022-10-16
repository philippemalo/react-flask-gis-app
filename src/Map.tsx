import React, { useEffect } from "react";
import mapboxgl from "mapbox-gl";
import { withRouter } from "react-router-dom";
import { MapContainer } from "./styles/MapContainer.css";
import { Toolbar } from "./Toolbar";

const Map = () => {
  useEffect(() => {
    mapboxgl.accessToken =
      "pk.eyJ1IjoicGhpbGlwcGVtYWxvIiwiYSI6ImNsOG9vc2U2djE1dnYzem95ODgwb2kxYW0ifQ.aTIs55RuZk5buE_i9ddoOg";
    const map = new mapboxgl.Map({
      container: "map", // container ID
      style: "mapbox://styles/mapbox/streets-v11", // style URL
      center: [-74.5, 40], // starting position [lng, lat]
      zoom: 9, // starting zoom
    });

    map.on("load", () => {
      map.addLayer({
        id: "terrain-data",
        type: "line",
        source: {
          type: "vector",
          url: "mapbox://mapbox.mapbox-terrain-v2",
        },
        "source-layer": "contour",
      });
    });

    map.on("click", (e) => console.log(e));
  }, []);

  return (
    <MapContainer id="map">
      <Toolbar />
    </MapContainer>
  );
};

export default withRouter(Map);
