/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export const $CreatePassenger = {
    properties: {
        type: {
            type: 'PassengerType',
            isRequired: true,
        },
        location: {
            type: 'string',
            isRequired: true,
        },
        distination: {
            type: 'string',
            isRequired: true,
        },
        payment_method: {
            type: 'string',
            isRequired: true,
        },
        pickup_date: {
            type: 'string',
            isRequired: true,
            format: 'date-time',
        },
        pickup_time: {
            type: 'string',
            isRequired: true,
            format: 'date-time',
        },
        pickup_location: {
            type: 'string',
            isRequired: true,
        },
        return_date: {
            type: 'string',
            isRequired: true,
            format: 'date-time',
        },
        return_time: {
            type: 'string',
            isRequired: true,
            format: 'date-time',
        },
        service_hours: {
            type: 'number',
            isRequired: true,
        },
    },
} as const;
