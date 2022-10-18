import { gql, useApolloClient } from "@apollo/client";
import { Card, CardContent, CardMedia, Typography } from "@mui/material";
import React, { useContext, useState } from "react";
import { UserContext } from "./App";
import { UserProjectsContainer } from "./styles/UserProjectsContainer.css";

type Project = {
  id: number;
  name: string;
};

export const UserProjects = () => {
  const [projects, setProjects] = useState([]);
  const client = useApolloClient();

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

  // Fetch user projects

  return (
    <UserContext.Consumer>
      {(value) => {
        if (!value.authed) {
          window.location.replace("/login");
        } else {
          return (
            <UserProjectsContainer>
              {projects.map((project: Project) => (
                <Card key={project.id} sx={{ maxWidth: 345 }}>
                  <CardMedia
                    component="img"
                    height="140"
                    image="https://images.landscapingnetwork.com/pictures/images/900x705Max/site_8/oxford-college-of-garden-design_3126.jpg"
                    alt={project.name}
                  />
                  <CardContent>
                    <Typography gutterBottom variant="h5" component="div">
                      {project.name}
                    </Typography>
                  </CardContent>
                </Card>
              ))}
            </UserProjectsContainer>
          );
        }
      }}
    </UserContext.Consumer>
  );
};
