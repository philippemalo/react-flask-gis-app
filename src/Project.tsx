import React from "react";
import { useParams } from "react-router-dom";
import { Loader } from "./Loader";
import Map from "./Map";

const Project = () => {
  const { projectid } = useParams();

  if (!!projectid) {
    return <Map projectId={projectid} />;
  } else {
    return <Loader />;
  }
};

export default Project;
