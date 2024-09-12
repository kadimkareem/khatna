import {
    Container,
    Flex,
    Heading,
    Spinner,
    Table,
    TableContainer,
    Tbody,
    Td,
    Th,
    Thead,
    Tr,
} from '@chakra-ui/react'
import { createFileRoute } from '@tanstack/react-router'
import { useQuery } from 'react-query'

import { ApiError, CarsService } from '../../client'  // Import CarsService
import ActionsMenu from '../../components/Common/ActionsMenu'
import Navbar from '../../components/Common/Navbar'
import useCustomToast from '../../hooks/useCustomToast'

//refactor the code
export const Route = createFileRoute('/_layout/cars')({
    component: Cars,
})

function Cars() {
    const showToast = useCustomToast()
    const {
        data: cars,
        isLoading,
        isError,
        error,
    } = useQuery('cars', () => CarsService.readCars({}))  // Use CarsService to fetch data

    if (isError) {
        const errDetail = (error as ApiError).body?.detail
        showToast('Something went wrong.', `${errDetail}`, 'error')
    }

    return (
        <>
            {isLoading ? (
                // TODO: Add skeleton
                <Flex justify="center" align="center" height="100vh" width="full">
                    <Spinner size="xl" color="ui.main" />
                </Flex>
            ) : (
                cars && (
                    <Container maxW="full">
                        <Heading
                            size="lg"
                            textAlign={{ base: 'center', md: 'left' }}
                            pt={12}
                        >
                            Cars Management
                        </Heading>
                        <Navbar type={'Car'} />
                        <TableContainer>
                            <Table size={{ base: 'sm', md: 'md' }}>
                                <Thead>
                                    <Tr>
                                        <Th>ID</Th>
                                        <Th>Model</Th>
                                        <Th>License Plate</Th>
                                        <Th>Year</Th>
                                        <Th>Color</Th>
                                        <Th>Capacity</Th>
                                        <Th>Type</Th>
                                        <Th>Actions</Th>
                                    </Tr>
                                </Thead>
                                <Tbody>
                                    {cars.data.map((car) => (
                                        <Tr key={car.id}>
                                            <Td>{car.id}</Td>
                                            <Td>{car.model || 'N/A'}</Td>
                                            <Td>{car.license_plate || 'N/A'}</Td>
                                            <Td>{car.year || 'N/A'}</Td>
                                            <Td>{car.color || 'N/A'}</Td>
                                            <Td>{car.capacity || 'N/A'}</Td>
                                            <Td>{car.type ? car.type : 'N/A'}</Td>  {/* Assuming car.type has a name property */}
                                            <Td>
                                                <ActionsMenu type={'Car'} value={car} />
                                            </Td>
                                        </Tr>
                                    ))}
                                </Tbody>
                            </Table>
                        </TableContainer>
                    </Container>
                )
            )}
        </>
    )
}

export default Cars