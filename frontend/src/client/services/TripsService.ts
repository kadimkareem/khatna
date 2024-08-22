/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { TripCreate } from '../models/trip/TripCreate';
import type { TripOut } from '../models/trip/TripOut';
import type { TripsOUt } from '../models/trip/TripsOut';
import type { TripUpdate } from '../models/trip/TripUpdate';
import type { Message } from '../models//Message';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class TripsService {

    /**
     * Read Trips
     * Retrieve trips.
     * @returns TripsOut Successful Response
     * @throws ApiError
     */
    public static readTrips({
        skip,
        limit = 100,
    }: {
        skip?: number,
        limit?: number,
    }): CancelablePromise<TripsOUt> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/trips/',
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
     * Create Trip
     * Create new trip.
     * @returns TripOut Successful Response
     * @throws ApiError
     */
    public static createTrip({
        requestBody,
    }: {
        requestBody: TripCreate,
    }): CancelablePromise<TripOut> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/trips/',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Read Trip
     * Get trip by ID.
     * @returns TripOut Successful Response
     * @throws ApiError
     */
    public static readTrip({
        id,
    }: {
        id: number,
    }): CancelablePromise<TripOut> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/trips/{id}',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Update Trip
     * Update an trip.
     * @returns TripOut Successful Response
     * @throws ApiError
     */
    public static updateTrip({
        id,
        requestBody,
    }: {
        id: number,
        requestBody: TripUpdate,
    }): CancelablePromise<TripOut> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/trips/{id}',
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
     * Delete Trip
     * Delete an trip.
     * @returns Message Successful Response
     * @throws ApiError
     */
    public static deleteTrip({
        id,
    }: {
        id: number,
    }): CancelablePromise<Message> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/trips/{id}',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
