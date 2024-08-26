/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export const $RouteCreate = {
    properties: {
        start: {
            type: 'number',
            isRequired: true,
        },
        end: {
            type: 'number',
            isRequired: true,
        },
        path: {
            type: 'any-of',
            contains: [{
                type: 'array',
                contains: {
                    type: 'string',
                },
            }, {
                type: 'null',
            }],
        },
    },
} as const;
