/* eslint-disable */
import * as types from './graphql';
import { TypedDocumentNode as DocumentNode } from '@graphql-typed-document-node/core';

const documents = {
    "\n  mutation createUserMutationDocument($email: String!, $password: String!) {\n    createUser(email: $email, password: $password) {\n      success\n      errors\n      user {\n        id\n        email\n      }\n    }\n  }\n": types.CreateUserMutationDocumentDocument,
    "\n  mutation createProjectMutationDocument($projectName: String!, $userId: ID!) {\n    createProject(projectName: $projectName, userId: $userId) {\n      success\n      errors\n      project {\n        id\n        name\n      }\n    }\n  }\n": types.CreateProjectMutationDocumentDocument,
    "\n  query isConnectedQueryDocument {\n    isConnected {\n      success\n      errors\n      user {\n        id\n        email\n      }\n    }\n  }\n": types.IsConnectedQueryDocumentDocument,
    "\n  query userLoginQueryDocument($email: String!, $password: String!) {\n    userLogin(email: $email, password: $password) {\n      success\n      errors\n      user {\n        id\n        email\n      }\n    }\n  }\n": types.UserLoginQueryDocumentDocument,
    "\n  query userProjectsQueryDocument($userId: ID!) {\n    userProjects(userId: $userId) {\n      success\n      errors\n      projects {\n        id\n        name\n      }\n    }\n  }\n": types.UserProjectsQueryDocumentDocument,
};

export function graphql(source: "\n  mutation createUserMutationDocument($email: String!, $password: String!) {\n    createUser(email: $email, password: $password) {\n      success\n      errors\n      user {\n        id\n        email\n      }\n    }\n  }\n"): (typeof documents)["\n  mutation createUserMutationDocument($email: String!, $password: String!) {\n    createUser(email: $email, password: $password) {\n      success\n      errors\n      user {\n        id\n        email\n      }\n    }\n  }\n"];
export function graphql(source: "\n  mutation createProjectMutationDocument($projectName: String!, $userId: ID!) {\n    createProject(projectName: $projectName, userId: $userId) {\n      success\n      errors\n      project {\n        id\n        name\n      }\n    }\n  }\n"): (typeof documents)["\n  mutation createProjectMutationDocument($projectName: String!, $userId: ID!) {\n    createProject(projectName: $projectName, userId: $userId) {\n      success\n      errors\n      project {\n        id\n        name\n      }\n    }\n  }\n"];
export function graphql(source: "\n  query isConnectedQueryDocument {\n    isConnected {\n      success\n      errors\n      user {\n        id\n        email\n      }\n    }\n  }\n"): (typeof documents)["\n  query isConnectedQueryDocument {\n    isConnected {\n      success\n      errors\n      user {\n        id\n        email\n      }\n    }\n  }\n"];
export function graphql(source: "\n  query userLoginQueryDocument($email: String!, $password: String!) {\n    userLogin(email: $email, password: $password) {\n      success\n      errors\n      user {\n        id\n        email\n      }\n    }\n  }\n"): (typeof documents)["\n  query userLoginQueryDocument($email: String!, $password: String!) {\n    userLogin(email: $email, password: $password) {\n      success\n      errors\n      user {\n        id\n        email\n      }\n    }\n  }\n"];
export function graphql(source: "\n  query userProjectsQueryDocument($userId: ID!) {\n    userProjects(userId: $userId) {\n      success\n      errors\n      projects {\n        id\n        name\n      }\n    }\n  }\n"): (typeof documents)["\n  query userProjectsQueryDocument($userId: ID!) {\n    userProjects(userId: $userId) {\n      success\n      errors\n      projects {\n        id\n        name\n      }\n    }\n  }\n"];

export function graphql(source: string): unknown;
export function graphql(source: string) {
  return (documents as any)[source] ?? {};
}

export type DocumentType<TDocumentNode extends DocumentNode<any, any>> = TDocumentNode extends DocumentNode<  infer TType,  any>  ? TType  : never;