import { TextField } from "@mui/material";
import React from "react";
import { UserContext } from "./App";
import { ProfileContainer } from "./styles/ProfileContainer.css";

export const Profile = () => {
  return (
    <UserContext.Consumer>
      {(value) => {
        if (!value.email) {
          window.location.replace("/login");
        } else {
          return (
            <ProfileContainer>
              <div
                style={{
                  display: "flex",
                  flexDirection: "column",
                  alignItems: "center",
                  justifyContent: "center",
                }}
              >
                <TextField
                  InputProps={{ readOnly: true }}
                  label="Email address"
                  defaultValue={value.email}
                />
              </div>
            </ProfileContainer>
          );
        }
      }}
    </UserContext.Consumer>
  );
};
