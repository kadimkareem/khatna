/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export const $TripUpdate_Input = {
    properties: {
        route_id: {
            type: 'any-of',
            contains: [{
                type: 'number',
            }, {
                type: 'null',
            }],
        },
        car_id: {
            type: 'any-of',
            contains: [{
                type: 'number',
            }, {
                type: 'null',
            }],
        },
        estimation: {
            type: 'any-of',
            contains: [{
                type: 'string',
                format: 'date-time',
            }, {
                type: 'null',
            }],
        },
        cost: {
            type: 'any-of',
            contains: [{
                type: 'number',
            }, {
                type: 'null',
            }],
        },
        tripStatus: {
            type: 'any-of',
            contains: [{
                type: 'TripStatus',
            }, {
                type: 'null',
            }],
        },
        type: {
            type: 'any-of',
            contains: [{
                type: 'TripType',
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
        passengers_count: {
            type: 'any-of',
            contains: [{
                type: 'number',
            }, {
                type: 'null',
            }],
        },
    },
} as const;
