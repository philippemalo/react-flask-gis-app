import { gql, useApolloClient } from "@apollo/client";
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

type Project = {
  id: number;
  name: string;
};

export const UserProjects = () => {
  const [projects, setProjects] = useState([]);
  const client = useApolloClient();
  const [showCreateProjectModal, setShowCreateProjectModal] = useState(false);
  const [newProjectName, setNewProjectName] = useState("");

  const connectedUser = useContext(UserContext);

  client
    .query({
      query: gql`
    query fetchUserProjects {
      userProjects(userId: "${connectedUser.user.id}") {
        success
        errors
        projects {
          id
          name
        }
      }
    }
    `,
    })
    .then((res) => setProjects(res.data.userProjects.projects));

  const modalStyle = {
    display: "flex",
    flexDirection: "column",
    position: "absolute" as "absolute",
    top: "50%",
    left: "50%",
    transform: "translate(-50%, -50%)",
    bgcolor: "background.paper",
    border: "1px solid #000",
    boxShadow: 24,
    p: 3,
    gap: "10px",
  };

  const handleCreateProject = () => {
    client
      .mutate({
        mutation: gql`
          mutation createProject {
            createProject(projectName: "${newProjectName}", userId: "${connectedUser.user.id}") {
              success
              errors
              project {
                id
                name
              }
            }
          }
        `,
      })
      .then((res) => {
        setShowCreateProjectModal(false);
        console.log(res);
      });
  };

  const handleCloseModal = () => {
    setShowCreateProjectModal(false);
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
                open={showCreateProjectModal}
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
                    Choose a name for your new project
                  </Typography>
                  <TextField
                    id="newproject"
                    label="Project name"
                    variant="standard"
                    onChange={(e) => setNewProjectName(e.currentTarget.value)}
                  />
                  <div
                    style={{
                      display: "flex",
                      justifyContent: "flex-end",
                    }}
                  >
                    <Button
                      onClick={handleCreateProject}
                      disabled={!newProjectName}
                    >
                      Create
                    </Button>
                    <Button onClick={() => setShowCreateProjectModal(false)}>
                      Cancel
                    </Button>
                  </div>
                </Box>
              </Modal>
              <UserProjectsContainer>
                <Card
                  key={"new project"}
                  sx={{ width: 250, height: 200 }}
                  onClick={() => setShowCreateProjectModal(true)}
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
                      {"New project"}
                    </Typography>
                  </CardContent>
                </Card>
                {projects.map((project: Project) => (
                  <Card key={project.id} sx={{ width: 250, height: 200 }}>
                    <CardMedia
                      component="img"
                      height="140"
                      image="https://images.landscapingnetwork.com/pictures/images/900x705Max/site_8/oxford-college-of-garden-design_3126.jpg"
                      alt={project.name}
                    />
                    <CardContent>
                      <Typography variant="h5" component="div">
                        {project.name}
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
