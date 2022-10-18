import { gql, useApolloClient } from "@apollo/client";
import { Alert, Button, Snackbar, TextField } from "@mui/material";
import React, { useState } from "react";
import { UserContext } from "./App";
import { RegisterContainer } from "./styles/RegisterContainer.css";

const validateEmail = (email: string) => {
  return String(email)
    .toLowerCase()
    .match(
      /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    );
};

export const Register = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showAlert, setShowAlert] = useState(false);

  const client = useApolloClient();

  const handleRegister = () => {
    const isValid = validateEmail(email);

    if (!isValid) {
      setShowAlert(true);
      return;
    }

    client
      .mutate({
        mutation: gql`
        mutation createUser {
          createUser(email: "${email}", password: "${password}") {
            success
            errors
            user {
              id
              email
            }
          }
        }
      `,
      })
      .then((res) =>
        res?.data?.createUser?.success
          ? window.location.replace("/home")
          : console.log("wrong creds")
      );
  };

  const handleClose = (
    event?: React.SyntheticEvent | Event,
    reason?: string
  ) => {
    if (reason === "clickaway") {
      return;
    }
    setShowAlert(false);
  };

  return (
    <UserContext.Consumer>
      {(value) => {
        if (value.authed) {
          window.location.replace("/home");
        } else {
          return (
            <RegisterContainer>
              <TextField
                id="email"
                label="EMAIL"
                variant="outlined"
                onChange={(e) => setEmail(e.currentTarget.value)}
              ></TextField>
              <TextField
                id="password"
                label="PASSWORD"
                variant="outlined"
                type="password"
                onChange={(e) => setPassword(e.currentTarget.value)}
              ></TextField>
              <Button variant="contained" onClick={handleRegister}>
                Register
              </Button>
              <Snackbar
                open={showAlert}
                autoHideDuration={6000}
                onClose={handleClose}
              >
                <Alert
                  onClose={handleClose}
                  severity="error"
                  sx={{ width: "100%" }}
                >
                  The email/password is invalid
                </Alert>
              </Snackbar>
            </RegisterContainer>
          );
        }
      }}
    </UserContext.Consumer>
  );
};
