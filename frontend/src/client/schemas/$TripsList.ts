/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export const $TripsList = {
    properties: {
        trips: {
            type: 'array',
            contains: {
                type: 'Trip',
            },
            isRequired: true,
        },
        count: {
            type: 'any-of',
            contains: [{
                type: 'number',
            }, {
                type: 'null',
            }],
        },
    },
} as const;
