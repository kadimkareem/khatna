/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export const $TripCreate_Input = {
    properties: {
        route_id: {
            type: 'number',
            isRequired: true,
        },
        car_id: {
            type: 'number',
            isRequired: true,
        },
        estimation: {
            type: 'string',
            isRequired: true,
            format: 'date-time',
        },
        cost: {
            type: 'number',
            isRequired: true,
        },
        tripStatus: {
            type: 'TripStatus',
            isRequired: true,
        },
        type: {
            type: 'TripType',
            isRequired: true,
        },
        passengers_count: {
            type: 'any-of',
            contains: [{
                type: 'number',
            }, {
                type: 'null',
            }],
        },
        passengers: {
            type: 'any-of',
            contains: [{
                type: 'array',
                contains: {
                    type: 'Passenger',
                },
            }, {
                type: 'null',
            }],
        },
    },
} as const;
