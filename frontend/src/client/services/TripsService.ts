/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Message } from '../models/Message';
import type { Trip } from '../models/Trip';
import type { TripCreate_Input } from '../models/TripCreate_Input';
import type { TripCreate_Output } from '../models/TripCreate_Output';
import type { TripsList } from '../models/TripsList';
import type { TripUpdate_Input } from '../models/TripUpdate_Input';
import type { TripUpdate_Output } from '../models/TripUpdate_Output';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class TripsService {

    /**
     * Read Trips
     * Retrieve trips. only admin can fetch all
     * @returns TripsList Successful Response
     * @throws ApiError
     */
    public static readTrips({
        skip,
        limit = 100,
    }: {
        skip?: number,
        limit?: number,
    }): CancelablePromise<TripsList> {
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
     * @returns TripCreate_Output Successful Response
     * @throws ApiError
     */
    public static createTrip({
        requestBody,
    }: {
        requestBody: TripCreate_Input,
    }): CancelablePromise<TripCreate_Output> {
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
     * @returns Trip Successful Response
     * @throws ApiError
     */
    public static readTrip({
        id,
    }: {
        id: number,
    }): CancelablePromise<Trip> {
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
     * @returns TripUpdate_Output Successful Response
     * @throws ApiError
     */
    public static updateTrip({
        id,
        requestBody,
    }: {
        id: number,
        requestBody: TripUpdate_Input,
    }): CancelablePromise<TripUpdate_Output> {
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
