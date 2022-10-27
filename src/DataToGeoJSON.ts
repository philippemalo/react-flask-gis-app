import { Feature } from "./gql/graphql";

export const FeatureCollectionToGeoJSON = (
  FeatureCollection: Feature[]
): GeoJSON.FeatureCollection => {
  const formattedFeature = (feature: Feature): GeoJSON.Feature => {
    const geometryType: any = feature.geometry.type;
    return {
      id: feature.id,
      type: "Feature",
      properties: JSON.parse(feature.properties),
      geometry: {
        type: geometryType,
        coordinates: feature.geometry.coordinates,
      },
    };
  };

  const geojson: GeoJSON.FeatureCollection = {
    type: "FeatureCollection",
    features: FeatureCollection.map((feature) => {
      return formattedFeature(feature);
    }),
  };

  return geojson;
};
