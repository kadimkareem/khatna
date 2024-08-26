/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Message } from '../models/Message';
import type { Route } from '../models/Route';
import type { RouteCreate } from '../models/RouteCreate';
import type { RoutesOut } from '../models/RoutesOut';
import type { RouteUpdate } from '../models/RouteUpdate';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class RoutesService {

    /**
     * Read Routes
     * Retrieve routes.
     * @returns RoutesOut Successful Response
     * @throws ApiError
     */
    public static routesReadRoutes({
        skip,
        limit = 100,
    }: {
        skip?: number,
        limit?: number,
    }): CancelablePromise<RoutesOut> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/routes/',
            query: {
                'skip': skip,
                'limit': limit,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Create Route
     * Create new route.
     * @returns RouteCreate Successful Response
     * @throws ApiError
     */
    public static routesCreateRoute({
        requestBody,
    }: {
        requestBody: RouteCreate,
    }): CancelablePromise<RouteCreate> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/routes/',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Read Route
     * Get route by ID. any one can get route
     * @returns Route Successful Response
     * @throws ApiError
     */
    public static routesReadRoute({
        id,
    }: {
        id: number,
    }): CancelablePromise<Route> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/routes/{id}',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Update Route
     * Update an route.
     * @returns RouteUpdate Successful Response
     * @throws ApiError
     */
    public static routesUpdateRoute({
        id,
        requestBody,
    }: {
        id: number,
        requestBody: RouteUpdate,
    }): CancelablePromise<RouteUpdate> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/routes/{id}',
            path: {
                'id': id,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Delete Route
     * Delete an route.
     * @returns Message Successful Response
     * @throws ApiError
     */
    public static routesDeleteRoute({
        id,
    }: {
        id: number,
    }): CancelablePromise<Message> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/routes/{id}',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Find Routes Near Location
     * @returns any Successful Response
     * @throws ApiError
     */
    public static routesFindRoutesNearLocation({
        location,
    }: {
        location: string,
    }): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/routes/near/{location}',
            path: {
                'location': location,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
