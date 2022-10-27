import { useMutation, useQuery } from "@apollo/client";
import {
  Box,
  Button,
  Card,
  CardContent,
  CardMedia,
  Modal,
  TextField,
  Typography,
} from "@mui/material";
import React, { useContext, useState } from "react";
import { UserContext } from "./App";
import { UserProjectsContainer } from "./styles/UserProjectsContainer.css";
import AddIcon from "@mui/icons-material/Add";
import { userModelsQueryDocument } from "./graphql-types/queries";
import { createModelMutationDocument } from "./graphql-types/mutations";

const UserModels = () => {
  const [showCreateModelModal, setShowCreateModelModal] = useState(false);
  const [newModelName, setNewModelName] = useState("");

  const connectedUser = useContext(UserContext);

  const [createModel] = useMutation(createModelMutationDocument);

  const { data, refetch } = useQuery(userModelsQueryDocument, {
    variables: { userId: connectedUser.user.id },
  });

  const modalStyle = {
    display: "flex",
    flexDirection: "column",
    position: "absolute" as "absolute",
    top: "50%",
    left: "50%",
    transform: "translate(-50%, -50%)",
    bgcolor: "background.paper",
    boxShadow: 24,
    p: 3,
    gap: "10px",
  };

  const handleCreateModel = () => {
    createModel({
      variables: { modelName: newModelName, userId: connectedUser.user.id },
    }).then((res) => {
      refetch({ userId: connectedUser.user.id });
      setShowCreateModelModal(false);
    });
  };

  const handleCloseModal = () => {
    setShowCreateModelModal(false);
  };

  const handleModelSelect = (projectId: string | undefined) => {
    console.log(`Access model ${projectId}`);
  };

  return (
    <UserContext.Consumer>
      {(value) => {
        if (!value.authed) {
          window.location.replace("/login");
        } else {
          return (
            <>
              <Modal
                open={showCreateModelModal}
                onClose={handleCloseModal}
                aria-labelledby="modal-modal-title"
                aria-describedby="modal-modal-description"
              >
                <Box sx={modalStyle}>
                  <Typography
                    id="modal-modal-title"
                    variant="h6"
                    component="h2"
                  >
                    Choose a name for your new model
                  </Typography>
                  <TextField
                    id="newpmodel"
                    label="Model name"
                    variant="standard"
                    onChange={(e) => setNewModelName(e.currentTarget.value)}
                  />
                  <div
                    style={{
                      display: "flex",
                      justifyContent: "flex-end",
                    }}
                  >
                    <Button
                      onClick={handleCreateModel}
                      disabled={!newModelName}
                    >
                      Create
                    </Button>
                    <Button onClick={() => setShowCreateModelModal(false)}>
                      Cancel
                    </Button>
                  </div>
                </Box>
              </Modal>
              <UserProjectsContainer>
                <Card
                  key={"new project"}
                  sx={{ width: 250, height: 200 }}
                  onClick={() => setShowCreateModelModal(true)}
                  style={{ cursor: "pointer" }}
                >
                  <CardContent
                    style={{
                      display: "flex",
                      flexDirection: "column",
                      alignItems: "center",
                      justifyContent: "center",
                      height: "100%",
                      padding: 0,
                    }}
                  >
                    <AddIcon fontSize="large" color="primary" />
                    <Typography variant="h5" component="div">
                      {"New model"}
                    </Typography>
                  </CardContent>
                </Card>
                {data?.userModels?.models?.map((model) => (
                  <Card
                    key={model?.id}
                    sx={{ width: 250, height: 200 }}
                    style={{ cursor: "pointer" }}
                    onClick={() => handleModelSelect(model?.id)}
                  >
                    <CardMedia
                      component="img"
                      height="140"
                      image="https://www.clipartmax.com/png/middle/3-36982_tree-01-top-view-tree-icon.png"
                      alt={model?.name}
                    />
                    <CardContent>
                      <Typography variant="h5" component="div">
                        {model?.name}
                      </Typography>
                    </CardContent>
                  </Card>
                ))}
              </UserProjectsContainer>
            </>
          );
        }
      }}
    </UserContext.Consumer>
  );
};

export default UserModels;
