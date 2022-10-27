import React, { useEffect } from "react";
import mapboxgl from "mapbox-gl";
import { MapContainer } from "./styles/MapContainer.css";
import { Toolbar } from "./Toolbar";
import { useQuery } from "@apollo/client";
import { projectQueryDocument } from "./graphql-types/queries";
import { FeatureCollectionToGeoJSON } from "./DataToGeoJSON";
interface MapProps {
  projectId: string;
}

const Map = (props: MapProps) => {
  const { data, loading } = useQuery(projectQueryDocument, {
    variables: { projectId: props.projectId },
  });

  console.log(
    "WAZAAAA: ",
    data?.project?.project?.models[0]?.featureCollection[0]
  );

  useEffect(() => {
    mapboxgl.accessToken =
      "pk.eyJ1IjoicGhpbGlwcGVtYWxvIiwiYSI6ImNsOG9vc2U2djE1dnYzem95ODgwb2kxYW0ifQ.aTIs55RuZk5buE_i9ddoOg";
    const map = new mapboxgl.Map({
      container: "map", // container ID
      style: "mapbox://styles/mapbox/streets-v11", // style URL
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

      if (!loading) {
        console.log("beep boop");
        map.addSource("project-data", {
          type: "geojson",
          data: FeatureCollectionToGeoJSON(
            data.project.project.models[0].featureCollection
          ),
        });
      }
    });

    map.on("click", (e) => console.log(e));
  }, [data, loading]);

  return (
    <MapContainer id="map">
      <Toolbar />
    </MapContainer>
  );
};

export default Map;
