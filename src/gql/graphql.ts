/* eslint-disable */
import { TypedDocumentNode as DocumentNode } from '@graphql-typed-document-node/core';
export type Maybe<T> = T | null;
export type InputMaybe<T> = Maybe<T>;
export type Exact<T extends { [key: string]: unknown }> = { [K in keyof T]: T[K] };
export type MakeOptional<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]?: Maybe<T[SubKey]> };
export type MakeMaybe<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]: Maybe<T[SubKey]> };
/** All built-in and custom scalars, mapped to their actual values */
export type Scalars = {
  ID: string;
  String: string;
  Boolean: boolean;
  Int: number;
  Float: number;
};

export type Coordinates = {
  __typename?: 'Coordinates';
  latitude: Scalars['Float'];
  longitude: Scalars['Float'];
};

export type CreateModelResult = {
  __typename?: 'CreateModelResult';
  errors?: Maybe<Array<Maybe<Scalars['String']>>>;
  model?: Maybe<Model>;
  success: Scalars['Boolean'];
};

export type CreateProjectResult = {
  __typename?: 'CreateProjectResult';
  errors?: Maybe<Array<Maybe<Scalars['String']>>>;
  project?: Maybe<Project>;
  success: Scalars['Boolean'];
};

/** Mutation results types */
export type CreateUserResult = {
  __typename?: 'CreateUserResult';
  errors?: Maybe<Array<Maybe<Scalars['String']>>>;
  success: Scalars['Boolean'];
  user?: Maybe<User>;
};

export type DeletetionResult = {
  __typename?: 'DeletetionResult';
  errors?: Maybe<Array<Maybe<Scalars['String']>>>;
  success: Scalars['Boolean'];
};

/** Enums */
export enum GeometryType {
  Curve = 'CURVE',
  Geometry = 'GEOMETRY',
  Geometrycollection = 'GEOMETRYCOLLECTION',
  Linestring = 'LINESTRING',
  Multilinestring = 'MULTILINESTRING',
  Multipoint = 'MULTIPOINT',
  Multipolygon = 'MULTIPOLYGON',
  Point = 'POINT',
  Polygon = 'POLYGON'
}

export type Linestring = {
  __typename?: 'Linestring';
  geom: Array<Coordinates>;
  id: Scalars['ID'];
};

export type Model = {
  __typename?: 'Model';
  features: ModelFeatureCollection;
  id: Scalars['ID'];
  name: Scalars['String'];
};

export type ModelFeatureCollection = {
  __typename?: 'ModelFeatureCollection';
  linestrings?: Maybe<Array<Maybe<ModelLinestring>>>;
  points?: Maybe<Array<Maybe<ModelPoint>>>;
  polygons?: Maybe<Array<Maybe<ModelPolygon>>>;
};

export type ModelLinestring = {
  __typename?: 'ModelLinestring';
  geom: Array<Coordinates>;
  id: Scalars['ID'];
};

export type ModelPoint = {
  __typename?: 'ModelPoint';
  geom: Coordinates;
  id: Scalars['ID'];
};

export type ModelPolygon = {
  __typename?: 'ModelPolygon';
  geom: Array<Array<Coordinates>>;
  id: Scalars['ID'];
};

export type Mutation = {
  __typename?: 'Mutation';
  createModel: CreateModelResult;
  createProject: CreateProjectResult;
  createUser: CreateUserResult;
  deleteModel: DeletetionResult;
  deleteProject: DeletetionResult;
};


export type MutationCreateModelArgs = {
  modelName: Scalars['String'];
  userId: Scalars['ID'];
};


export type MutationCreateProjectArgs = {
  projectName: Scalars['String'];
  userId: Scalars['ID'];
};


export type MutationCreateUserArgs = {
  email: Scalars['String'];
  password: Scalars['String'];
};


export type MutationDeleteModelArgs = {
  modelId: Scalars['ID'];
  userId: Scalars['ID'];
};


export type MutationDeleteProjectArgs = {
  projectId: Scalars['ID'];
  userId: Scalars['ID'];
};

export type Point = {
  __typename?: 'Point';
  geom: Coordinates;
  id: Scalars['ID'];
};

export type Polygon = {
  __typename?: 'Polygon';
  geom: Array<Array<Coordinates>>;
  id: Scalars['ID'];
};

export type Project = {
  __typename?: 'Project';
  features: ProjectFeatureCollection;
  id: Scalars['ID'];
  models?: Maybe<Array<Maybe<ProjectModel>>>;
  name: Scalars['String'];
};

export type ProjectFeatureCollection = {
  __typename?: 'ProjectFeatureCollection';
  linestrings?: Maybe<Array<Maybe<Linestring>>>;
  points?: Maybe<Array<Maybe<Point>>>;
  polygons?: Maybe<Array<Maybe<Polygon>>>;
};

export type ProjectModel = {
  __typename?: 'ProjectModel';
  centerPoint: Coordinates;
  id: Scalars['ID'];
  model: Model;
  rotation: Scalars['Float'];
};

export type Query = {
  __typename?: 'Query';
  allModels?: Maybe<UserModelsResult>;
  isConnected?: Maybe<UserLoginResult>;
  userLogin?: Maybe<UserLoginResult>;
  userLogout?: Maybe<UserLoginResult>;
  userModels?: Maybe<UserModelsResult>;
  userProjects: UserProjectsResult;
  users: UsersResult;
};


export type QueryUserLoginArgs = {
  email: Scalars['String'];
  password: Scalars['String'];
};


export type QueryUserModelsArgs = {
  userId: Scalars['ID'];
};


export type QueryUserProjectsArgs = {
  userId: Scalars['ID'];
};

/** Basic types */
export type User = {
  __typename?: 'User';
  email: Scalars['String'];
  id: Scalars['ID'];
  models?: Maybe<Array<Maybe<Model>>>;
  projects?: Maybe<Array<Maybe<Project>>>;
};

/** Query results types */
export type UserLoginResult = {
  __typename?: 'UserLoginResult';
  errors?: Maybe<Array<Maybe<Scalars['String']>>>;
  success: Scalars['Boolean'];
  user?: Maybe<User>;
};

export type UserModelsResult = {
  __typename?: 'UserModelsResult';
  errors?: Maybe<Array<Maybe<Scalars['String']>>>;
  models?: Maybe<Array<Maybe<Model>>>;
  success: Scalars['Boolean'];
};

export type UserProjectsResult = {
  __typename?: 'UserProjectsResult';
  errors?: Maybe<Array<Maybe<Scalars['String']>>>;
  projects?: Maybe<Array<Maybe<Project>>>;
  success: Scalars['Boolean'];
};

export type UsersResult = {
  __typename?: 'UsersResult';
  errors?: Maybe<Array<Maybe<Scalars['String']>>>;
  success: Scalars['Boolean'];
  users?: Maybe<Array<Maybe<User>>>;
};

export type CreateUserMutationDocumentMutationVariables = Exact<{
  email: Scalars['String'];
  password: Scalars['String'];
}>;


export type CreateUserMutationDocumentMutation = { __typename?: 'Mutation', createUser: { __typename?: 'CreateUserResult', success: boolean, errors?: Array<string | null> | null, user?: { __typename?: 'User', id: string, email: string } | null } };

export type CreateProjectMutationDocumentMutationVariables = Exact<{
  projectName: Scalars['String'];
  userId: Scalars['ID'];
}>;


export type CreateProjectMutationDocumentMutation = { __typename?: 'Mutation', createProject: { __typename?: 'CreateProjectResult', success: boolean, errors?: Array<string | null> | null, project?: { __typename?: 'Project', id: string, name: string } | null } };

export type CreateModelMutationDocumentMutationVariables = Exact<{
  modelName: Scalars['String'];
  userId: Scalars['ID'];
}>;


export type CreateModelMutationDocumentMutation = { __typename?: 'Mutation', createModel: { __typename?: 'CreateModelResult', success: boolean, errors?: Array<string | null> | null, model?: { __typename?: 'Model', id: string, name: string } | null } };

export type IsConnectedQueryDocumentQueryVariables = Exact<{ [key: string]: never; }>;


export type IsConnectedQueryDocumentQuery = { __typename?: 'Query', isConnected?: { __typename?: 'UserLoginResult', success: boolean, errors?: Array<string | null> | null, user?: { __typename?: 'User', id: string, email: string } | null } | null };

export type UserLoginQueryDocumentQueryVariables = Exact<{
  email: Scalars['String'];
  password: Scalars['String'];
}>;


export type UserLoginQueryDocumentQuery = { __typename?: 'Query', userLogin?: { __typename?: 'UserLoginResult', success: boolean, errors?: Array<string | null> | null, user?: { __typename?: 'User', id: string, email: string } | null } | null };

export type UserProjectsQueryDocumentQueryVariables = Exact<{
  userId: Scalars['ID'];
}>;


export type UserProjectsQueryDocumentQuery = { __typename?: 'Query', userProjects: { __typename?: 'UserProjectsResult', success: boolean, errors?: Array<string | null> | null, projects?: Array<{ __typename?: 'Project', id: string, name: string } | null> | null } };

export type UserModelsQueryDocumentQueryVariables = Exact<{
  userId: Scalars['ID'];
}>;


export type UserModelsQueryDocumentQuery = { __typename?: 'Query', userModels?: { __typename?: 'UserModelsResult', success: boolean, errors?: Array<string | null> | null, models?: Array<{ __typename?: 'Model', id: string, name: string } | null> | null } | null };

export type AllModelsQueryDocumentQueryVariables = Exact<{ [key: string]: never; }>;


export type AllModelsQueryDocumentQuery = { __typename?: 'Query', allModels?: { __typename?: 'UserModelsResult', success: boolean, errors?: Array<string | null> | null, models?: Array<{ __typename?: 'Model', id: string, name: string } | null> | null } | null };


export const CreateUserMutationDocumentDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"mutation","name":{"kind":"Name","value":"createUserMutationDocument"},"variableDefinitions":[{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"email"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"String"}}}},{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"password"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"String"}}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"createUser"},"arguments":[{"kind":"Argument","name":{"kind":"Name","value":"email"},"value":{"kind":"Variable","name":{"kind":"Name","value":"email"}}},{"kind":"Argument","name":{"kind":"Name","value":"password"},"value":{"kind":"Variable","name":{"kind":"Name","value":"password"}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"success"}},{"kind":"Field","name":{"kind":"Name","value":"errors"}},{"kind":"Field","name":{"kind":"Name","value":"user"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"email"}}]}}]}}]}}]} as unknown as DocumentNode<CreateUserMutationDocumentMutation, CreateUserMutationDocumentMutationVariables>;
export const CreateProjectMutationDocumentDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"mutation","name":{"kind":"Name","value":"createProjectMutationDocument"},"variableDefinitions":[{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"projectName"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"String"}}}},{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"userId"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"ID"}}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"createProject"},"arguments":[{"kind":"Argument","name":{"kind":"Name","value":"projectName"},"value":{"kind":"Variable","name":{"kind":"Name","value":"projectName"}}},{"kind":"Argument","name":{"kind":"Name","value":"userId"},"value":{"kind":"Variable","name":{"kind":"Name","value":"userId"}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"success"}},{"kind":"Field","name":{"kind":"Name","value":"errors"}},{"kind":"Field","name":{"kind":"Name","value":"project"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"name"}}]}}]}}]}}]} as unknown as DocumentNode<CreateProjectMutationDocumentMutation, CreateProjectMutationDocumentMutationVariables>;
export const CreateModelMutationDocumentDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"mutation","name":{"kind":"Name","value":"createModelMutationDocument"},"variableDefinitions":[{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"modelName"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"String"}}}},{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"userId"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"ID"}}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"createModel"},"arguments":[{"kind":"Argument","name":{"kind":"Name","value":"modelName"},"value":{"kind":"Variable","name":{"kind":"Name","value":"modelName"}}},{"kind":"Argument","name":{"kind":"Name","value":"userId"},"value":{"kind":"Variable","name":{"kind":"Name","value":"userId"}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"success"}},{"kind":"Field","name":{"kind":"Name","value":"errors"}},{"kind":"Field","name":{"kind":"Name","value":"model"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"name"}}]}}]}}]}}]} as unknown as DocumentNode<CreateModelMutationDocumentMutation, CreateModelMutationDocumentMutationVariables>;
export const IsConnectedQueryDocumentDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"query","name":{"kind":"Name","value":"isConnectedQueryDocument"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"isConnected"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"success"}},{"kind":"Field","name":{"kind":"Name","value":"errors"}},{"kind":"Field","name":{"kind":"Name","value":"user"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"email"}}]}}]}}]}}]} as unknown as DocumentNode<IsConnectedQueryDocumentQuery, IsConnectedQueryDocumentQueryVariables>;
export const UserLoginQueryDocumentDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"query","name":{"kind":"Name","value":"userLoginQueryDocument"},"variableDefinitions":[{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"email"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"String"}}}},{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"password"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"String"}}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"userLogin"},"arguments":[{"kind":"Argument","name":{"kind":"Name","value":"email"},"value":{"kind":"Variable","name":{"kind":"Name","value":"email"}}},{"kind":"Argument","name":{"kind":"Name","value":"password"},"value":{"kind":"Variable","name":{"kind":"Name","value":"password"}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"success"}},{"kind":"Field","name":{"kind":"Name","value":"errors"}},{"kind":"Field","name":{"kind":"Name","value":"user"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"email"}}]}}]}}]}}]} as unknown as DocumentNode<UserLoginQueryDocumentQuery, UserLoginQueryDocumentQueryVariables>;
export const UserProjectsQueryDocumentDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"query","name":{"kind":"Name","value":"userProjectsQueryDocument"},"variableDefinitions":[{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"userId"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"ID"}}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"userProjects"},"arguments":[{"kind":"Argument","name":{"kind":"Name","value":"userId"},"value":{"kind":"Variable","name":{"kind":"Name","value":"userId"}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"success"}},{"kind":"Field","name":{"kind":"Name","value":"errors"}},{"kind":"Field","name":{"kind":"Name","value":"projects"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"name"}}]}}]}}]}}]} as unknown as DocumentNode<UserProjectsQueryDocumentQuery, UserProjectsQueryDocumentQueryVariables>;
export const UserModelsQueryDocumentDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"query","name":{"kind":"Name","value":"userModelsQueryDocument"},"variableDefinitions":[{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"userId"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"ID"}}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"userModels"},"arguments":[{"kind":"Argument","name":{"kind":"Name","value":"userId"},"value":{"kind":"Variable","name":{"kind":"Name","value":"userId"}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"success"}},{"kind":"Field","name":{"kind":"Name","value":"errors"}},{"kind":"Field","name":{"kind":"Name","value":"models"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"name"}}]}}]}}]}}]} as unknown as DocumentNode<UserModelsQueryDocumentQuery, UserModelsQueryDocumentQueryVariables>;
export const AllModelsQueryDocumentDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"query","name":{"kind":"Name","value":"allModelsQueryDocument"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"allModels"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"success"}},{"kind":"Field","name":{"kind":"Name","value":"errors"}},{"kind":"Field","name":{"kind":"Name","value":"models"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"name"}}]}}]}}]}}]} as unknown as DocumentNode<AllModelsQueryDocumentQuery, AllModelsQueryDocumentQueryVariables>;