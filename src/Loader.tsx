import { CircularProgress } from "@mui/material";
import React from "react";

export const Loader = () => {
  return (
    <div
      style={{
        display: "flex",
        height: "100vh",
        width: "100vw",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      <CircularProgress />
    </div>
  );
};
